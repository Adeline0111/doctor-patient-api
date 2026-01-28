from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    problem = models.TextField()
    medication = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
