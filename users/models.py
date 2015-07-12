from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.address
