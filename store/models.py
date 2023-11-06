from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


#Modificando la tabla user
class UserModel(AbstractUser):
    dni = models.CharField(max_length=12)
    email = models.CharField(max_length=254,unique=True)
    
    
    def __str__(self) -> str:
        return f"{self.username} ------ {self.email} ------ {self.dni}"



LAP = "Laptops"
COM = "Computadoras de mesa"
PER = "Perifericos"

choicess = (
    (LAP,"Laptops"),
    
    (COM,"Computadoras de mesa"),
    
    (PER,"Perifericos"),
    )

class Product(models.Model):
    productimage =models.ImageField(upload_to="store/images/",null=True) #SE LE AÑADE EL DIRECTORIO DONDE SE ALMACENARAN LAS IMG
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.FloatField()
    category = models.CharField(max_length=30,choices=choicess)
    views = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    belongs = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f" {self.name}   -----   ${self.price}   -----   {self.views}    -----   {self.belongs.email}"
    
    
    def __unicode__(self):
        return str(self.productimage)
    




class Mensaje(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="EMISOR")
    datesent = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)
    to = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return f"{self.author}--------{self.to}"