from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.AutoField(primary_key=True) 
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  description= models.TextField()
  

def __str__(self):
        return f'{self.id}: {self.firstname} {self.lastname}'