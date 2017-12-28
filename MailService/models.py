from django.db import models
import usr.models

# Create your models here.
#todo: clean up content of mail

class Mail(models.Model):
    receiver = models.ForeignKey('usr.Usr',on_delete=models.SET_NULL,null=True,related_name='mail_receiver')
    sender = models.ForeignKey('usr.Usr',on_delete=models.SET_NULL,null=True,related_name='mail_sender')
    content = models.CharField(max_length=1000)