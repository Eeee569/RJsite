from django.db import models

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
    tital = models.CharField(max_length=100)
    fileName = models.CharField(max_length=100)
    filePath = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    prompts = models.ManyToManyField(CollegePrompt)

    def __str__(self):
        return self.filename + self.id

