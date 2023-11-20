from django.db import models
from store.models import UserModel,Product

from django.conf import settings

# Create your models here.


#Tabla de lista de deseos

class ListaDeDeseo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    producto = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f"{self.usuario.username}  {self.producto.name}"
    



#Tabla de ventas


class Venta(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="vendedor_Venta")
    comprador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comprador_Venta")
    producto = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="producto_Venta")