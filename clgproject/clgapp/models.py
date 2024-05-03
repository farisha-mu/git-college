from django.db import models
from django.contrib.auth import get_user_model
usr = get_user_model()

# Create your models here.

class course(models.Model):
    course_name = models.CharField(max_length=200)



class teacher(models.Model):
    user = models.ForeignKey(usr,on_delete=models.CASCADE,null=True)
    course_fk = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    phnone = models.IntegerField()
    image = models.ImageField(upload_to='image/',null=True)
    join_date = models.DateField(auto_now_add=True)

class student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    course_fk=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='image/',null=True)