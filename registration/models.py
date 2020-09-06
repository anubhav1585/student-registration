from django.db import models

# Create your models here.
class Studentinfo(models.Model):
    name = models.CharField( max_length=50)
    father_n = models.CharField( max_length=50)
    mother_n = models.CharField( max_length=50)
    address = models.TextField()
    course = models.CharField( max_length=50)


class Studentmark(models.Model):
    name = models.CharField(max_length=100)
    maths = models.IntegerField()
    english = models.IntegerField() 
    hindi = models.IntegerField()
    social_science  = models.IntegerField()
    science  = models.IntegerField()
