from django.db import models
from django.contrib.auth.models import User
#from CollageApp.models import College
# toDo: ajusts max lenght for chars,update refs to other models

class Usr(models.Model):
    #uniId = models.IntegerField() django already does this with a.id
    #**********set true when implementing authentication*************user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    #userName = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Parent(Usr):
    #students = models.ManyToManyField(Student)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id


class Teacher(Usr):
    #students = models.ManyToManyField(Student)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id


class Student(Usr):
    #find students with s.student_set.all()(or .filter())
    colleges = models.ManyToManyField('CollageApp.College')
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)#set null may throw error
    parent = models.ForeignKey(Parent,on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id

