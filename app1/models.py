from django.db import models

# Create your models here.
class Addtask(models.Model):
    task=models.CharField(max_length=60)
    done=models.BooleanField(default=False)
    deadline=models.DateField(null=True,blank=True)