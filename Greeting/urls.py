from django.urls import path
from . import views as v

urlpatterns = [
    path("",v.welcome,name="Welcome"),
    
    path("about/",v.about,name="About"),
    
    path("computers/",v.computers,name="Computers"),
    
    path("laptops/",v.laptops,name="Laptops"),
    
    path("peripherals/",v.peripherals,name="Peripherals"),
    
    path("buyproducts/",v.buy,name="BUY"),
    
    path("añadirlista/",v.añadirlistadeseos,name="LISTA"),
    
    path("eliminarlista/",v.eliminarlistadeseos,name="ELIMINARLISTA"),
    
    path("Compra/",v.comprafunct,name="COMPRA")
    
]