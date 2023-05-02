from django.db import models
from django.urls import reverse

#A model is a python class that manages an underline database table.
#Bussiness logic: The main logic in the app. 

class Post(models.Model):                                   #example of inheritance
    title = models.CharField(max_length=128)                #multiple exameples of composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

#Create a model is not enought, we have to create a migration in admin.py
#and run the command in cmd: python3 manage.py makemigrations
#run migrations: python3 manage.py migrate

    def __str__(self):
        return self.title
    #We do not need a migration because this is a method and does not affects the db
    #This method is to change how we see the objects in the admin panel of django

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])