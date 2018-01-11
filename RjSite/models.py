from django.db import models
from django.contrib.auth.models import User
#from CollageApp.models import College
# toDo: ajusts max lenght for chars or update to TextField,update refs to other models

class Usr(models.Model):
    #uniId = models.IntegerField() django already does this with a.id
    #**********set true when implementing authentication*************user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    #userName = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    #class Meta: # i dont know if this has to be abstract, to referance by mail must not be abstract
        #abstract = True

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
    colleges = models.ManyToManyField('College')
    studentTeacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)#set null may throw error
    studentParent = models.ForeignKey(Parent,on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering = ('name','id',)

    def __str__(self):
        return self.name + self.id




# toDo: ajusts max lenght for chars, update refs to other models, make sure studentEssay always has a filename and filePath

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + self.id

    class Meta:
        ordering = ('name','id',)



class CollegePrompt(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    prompt = models.CharField(max_length=1000)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.prompt + self.id

    class Meta:
        ordering = ('name','id',)



class StudentEssay(models.Model): #all student essays must generate a file name and path to be valid
    title = models.CharField(max_length=100)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    fileName = models.CharField(max_length=100)
    filePath = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    prompts = models.ManyToManyField(CollegePrompt)
    coments = models.CharField(max_length=1000)
    def __str__(self):
        return self.filename + self.id

    class Meta:
        ordering = ('-time','title','id',)#-makes it descending



#todo: clean up content of mail

class Mail(models.Model):
    receiver = models.ForeignKey(Usr,on_delete=models.SET_NULL,null=True,related_name='mail_receiver')
    sender = models.ForeignKey(Usr,on_delete=models.SET_NULL,null=True,related_name='mail_sender')
    content = models.CharField(max_length=1000)


#todo: turn content into a pdf or possibly a billing service

class Bill(models.Model):
    billingTeacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    billingParent = models.ForeignKey(Parent,on_delete=models.SET_NULL,null=True)
    content = models.CharField(max_length=1000)
# Create your models here.

