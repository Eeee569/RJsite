from django.db import models

# toDo: ajusts max lenght for chars,

class Usr(models.Model):
    #uniId = models.IntegerField() django already does this with a.id
    email = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True



class Student(Usr):
    #find teachers with s.teacher_set.all()(or .filter())
    #find Parents with s.parent__set.all()...
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
