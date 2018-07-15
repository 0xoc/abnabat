from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE);
   #TODO: many to many to DInfo
    def __str__(self):
        return str(self.user)

class DeliverInfo(models.Model):
    startDate = models.DateField()
    endDate = models.DateField(null = True, blank = True)
    def __str__(self):
        return str(self.user)

class Client(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
