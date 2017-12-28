from django.db import models
from django.contrib.auth.models import User
from CollageApp.models import StudentEssay, College
# toDo: ajusts max lenght for chars,update refs to other models

class Usr(models.Model):
    #uniId = models.IntegerField() django already does this with a.id
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    #userName = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True



class Student(Usr):
    #find teachers with s.teacher_set.all()(or .filter())
    #find Parents with s.parent__set.all()...
    essays = models.ManyToManyField(StudentEssay)
    colleges = models.ManyToManyField(College)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id

class Parent(Usr):
    students = models.ManyToManyField(Student)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id


class Teacher(Usr):
    students = models.ManyToManyField(Student)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id

