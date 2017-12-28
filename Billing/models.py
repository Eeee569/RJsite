from django.db import models
from usr.models import Parent,Teacher

#todo: turn content into a pdf or possibly a billing service

class Bill(models.Model):
    teacher = models.ForeignKey('Teacher',on_delete=models.SET_NULL,null=True)
    parent = models.ForeignKey('Parent',on_delete=models.SET_NULL,null=True)
    content = models.CharField(max_length=1000)
# Create your models here.

