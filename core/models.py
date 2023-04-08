from django import forms
from django.db import models
from . import choices


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=117)
    size = models.CharField(max_length=40, choices=choices.SIZE_CHOICES)
    friendliness = models.IntegerField(choices=choices.CHOICES_1_TO_5);
    trainability = models.IntegerField(choices=choices.CHOICES_1_TO_5);
    sheddingamount = models.IntegerField(choices=choices.CHOICES_1_TO_5);
    exerciseneeds = models.IntegerField(choices=choices.CHOICES_1_TO_5);

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=117)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=choices.GENDER_CHOICES)
    color = models.CharField(max_length=117)
    favoritefood = models.CharField(max_length=117)
    favoritetoy = models.CharField(max_length=117)

    def __str__(self):
        return self.name
