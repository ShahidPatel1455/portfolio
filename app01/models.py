from django.db import models

# Create your models here.
class Contactwala(models.Model):
    name = models.CharField(max_length=25)
    email= models.EmailField()
    subject= models.TextField(max_length=50)
    message= models.TextField()

    def __str__(self):
        return self.name