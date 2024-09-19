from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/')


    def __str__(self):
        return self.name


class CarColor(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color
    

class Category(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Car(models.Model):
    name = models.CharField(max_length=200)
    produced_year = models.DateField()
    color = models.ForeignKey(CarColor,models.CASCADE,related_name='cars')
    price = models.PositiveIntegerField()
    case = models.CharField(max_length=100)  
    transmission = models.CharField(max_length=50) 
    location = models.CharField(max_length=200)
    brand = models.ForeignKey(CarBrand,models.CASCADE,related_name='cars')
    fuel = models.CharField(max_length=200,blank=True,null=True)
    category = models.ForeignKey(Category,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    car = models.CharField(max_length=200, blank=True)




   