from django.db import models


class Ingredient(models.Model):
    item = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredients/')
    calories = models.IntegerField()


    def __str__(self):
        return self.item 


class Meal(models.Model): 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals/')
    


    def __str__(self):
        return self.name