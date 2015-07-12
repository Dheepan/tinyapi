from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
from users.models import User,Address

@csrf_exempt
def create_user(request):
    user_data=json.loads(request.POST.get('data'))
    data=user_data['user']
    print type(data)
    username=data['username']
    fname=data['fname']
    lname=data['lname']
    u=User(username=username,fname=fname,lname=lname)
    u.save()
    address=data['address']
    for ad in address:
        a=Address(user_id=u,address=ad)
        a.save()
    return HttpResponse(status=201)

@csrf_exempt
def show_users(request):
    data={}
    results=User.objects.all()
    alldata=[]
    for u in results:
        data={'fname':u.fname,'lname':u.lname,'address':[]}
        addresses=Address.objects.filter(user_id=u.id)
        for a in addresses:
            data['address'].append(a.address)
        alldata.append(data)
    return HttpResponse(json.dumps({'users':alldata}), content_type="application/json")

@csrf_exempt
def user_details(request,userid=None):
    if userid is not None:
        try:
            u=User.objects.get(id=userid)
        except:
            return HttpResponse(json.dumps({'users':"User not found"}), content_type="application/json")
        data={}
        data['fname']=u.fname
        data['lname']=u.lname
        data['address']=[]
        addresses=Address.objects.filter(user_id=u.id)
        for a in addresses:
            data['address'].append(a.address)

    return HttpResponse(json.dumps({'users':data}), content_type="application/json")
