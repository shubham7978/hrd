from django.db import models
from django.utils import timezone
import datetime

class Company(models.Model):
 def __str__(self):
  return self.name
 name=models.CharField(max_length=100)
 address=models.CharField(max_length=200)
 description= models.CharField(max_length=1000)
 email=models.EmailField()

class Job(models.Model):
 def __str__(self):
  return self.title
 company=models.ForeignKey(Company, on_delete=models.CASCADE)
 title=models.CharField(max_length=50)
 description=models.CharField(max_length=1000)
 pub_date=models.DateField()
 duration=models.DurationField()
 qualification=models.CharField(max_length=200)
 requirements=models.CharField(max_length=1000)

 def was_published_recently(self):
  return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Create your models here.
