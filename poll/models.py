from django.db import models

# Create your models here.

class apollModel(models.Model):
    question = models.CharField(max_length=200,primary_key=True)
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)

class upollModel(models.Model):
    question = models.ForeignKey(apollModel,on_delete=models.CASCADE)
    choice = models.CharField(max_length=5,choices=(('good','good'),('bad','bad')),default='')
    vote = models.IntegerField(default=0)

class tpollModel(models.Model):
    question = models.ForeignKey(apollModel,on_delete=models.CASCADE)
    choice = models.CharField(max_length=5,choices=(('good','good'),('bad','bad')),default='')
    vote = models.IntegerField(default=0)