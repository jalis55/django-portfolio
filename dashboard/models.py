from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    email = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    languages = models.CharField(max_length=100)
    about = models.CharField(max_length=500)

class Skills(models.Model):
    skill_name=models.CharField(max_length=40)
    rating=models.IntegerField()

class WorkExprience(models.Model):
    from_to=models.CharField(max_length=20)
    organization=models.CharField(max_length=50)
    job_title=models.CharField(max_length=100)
    job_description=models.CharField(max_length=200)

class Education(models.Model):
    from_to=models.CharField(max_length=20)
    degree_name=models.CharField(max_length=50)
    degree_title=models.CharField(max_length=50)
    instituation=models.CharField(max_length=50)

class Reviews(models.Model):
    clients_name=models.CharField(max_length=30)
    organization=models.CharField(max_length=30)
    review_description=models.CharField(max_length=200)

    
 
 