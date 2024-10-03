from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Odontologo(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

class Blog(models.Model):
    title = models.CharField(max_length=200)  
    summary = models.TextField()  
    description = models.TextField()         
    image = models.ImageField(upload_to='assets/img/') 
    url = models.URLField()                    
    autor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title  