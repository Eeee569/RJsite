from django.db import models



class College(models.Model):
    Name = models.CharField(max_length=50)
    idUN = models.IntegerField()
    #get essays through cololegevar.essay_set.all()

class Essay(models.Model):
    collegeSource = models.ForeignKey(College, on_delete=models.CASCADE)
    prompt = models.CharField(max_length = 1000)#may need to increase




class Parent(models.Model):
    type = models.IntegerField()#1 for teacher, 2 for student and 3, for parent
    idUN = models.IntegerField()#
    userName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)

#s

    def __str__(self):
        return self.userName + ' - ' + self.id


class Teacher(models.Model):
    type = models.IntegerField()#1 for teacher, 2 for student and 3, for parent
    idUN = models.IntegerField()#
    userName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
#list thw rt dsfhjh the g ssaf


    def __str__(self):
        return self.userName + ' - ' + self.id

class Student(models.Model):
    type = models.IntegerField()#1 for teacher, 2 for student and 3, for parent
    idUN = models.IntegerField()#
    userName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)

    #many students to one
    child = models.ForeignKey(Parent, on_delete=models.CASCADE)  # acces through var(parentvar).student_set.all()
    teacher = models.ForeignKey(Teacher, null=True,on_delete=models.SET_NULL) #get students through teachervar.student_set.all()

    #many colleges to many sutdents
    colleges = models.ManyToManyField(College)
    #cascade will delete the item when teacher is deleted,set_null will just set this students teacher to null

    def __str__(self):
        return self.userName + ' - ' + self.id




class StudentEssay(models.Model):
    idUN = models.IntegerField()
    prompt = models.ForeignKey(Essay,null=True,on_delete=models.SET_NULL )
    studentSource = models.ForeignKey(Student,on_delete=models.CASCADE )
    pdfSrc = models.CharField(max_length=50)
