from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE);
    def __str__(self):
        return str(self.user)

class Deliver(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE);
    STATE = [('FR','FREE'),('OF','OFF'),('ON','ON DUTY')]
    status = models.CharField(max_length=10,choices=STATE,default='FR')
    def __str__(self):
        return str(self.user)

class Client(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
