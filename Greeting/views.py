from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from store.models import Product

from .models import ListaDeDeseo, Venta




#Muestra bienvenida al usuario guest(Puede mostrar productos mas comprados-Idea)
def welcome(request):
    
    return render(request,template_name="welcome.html")
   
      



#Muestra informacion sobre la empresa, desarrolladores, etc
def about(request):
    return render(request,template_name="about.html")

@login_required()
#Muestra apartado de computadoras
def computers(request):
    form = Product.objects.all()
    return render(request,template_name="computers.html",context={"form":form})

@login_required()
#Muestra apartado de laptops
def laptops(request):
    return render(request,template_name="laptops.html")

@login_required()
#Muestra apartado de perifericos
def peripherals(request):
    return render(request,template_name="peripherals.html")


@login_required
def buy(request):
    
    
    
    #Se puede hacer mejor el eliminar la lista de deseos utilizando el metodo get y el redirect
    if request.method == "GET":
        
        
        return render(request,template_name="buyproduct.html")
    else:
        
        
        
        
        print(request.POST)
        
        product = Product.objects.get(id=request.POST["product"])
        
        product.views += 1
        
        product.save()
        
        en_lista = ListaDeDeseo.objects.filter(usuario_id = request.user.id, producto = product)
        
        deseos = list(en_lista)
        
        print(en_lista)
        
        en_lista_ver = True
        
        
        print(deseos)
        
        if deseos == []:
            
            en_lista_ver = False
            
        print(en_lista_ver)
        
        
        return render(request,template_name="buyproduct.html",context={"product":product,"lista":en_lista_ver})


#Muestra los productos mas vistos
def most_viewed(request):
    return render(request,template_name="Most_viewed.html")



def añadirlistadeseos(request):
    
    if request.method == "GET":
        return redirect("BUY")
    
    else:
        
        
        productoid = request.POST["product"]
        
        producto = Product.objects.get(id=productoid)
        
        
        usuario = request.user.id
        
        ListaDeDeseo.objects.create(usuario_id=usuario,producto=producto)
        
        return render(request,template_name="buyproduct.html",context={"product":producto})
    

def eliminarlistadeseos(request):
    
    if request.method == "POST":
        
        productid = request.POST["product"]
        
        producto = Product.objects.get(id=productid)
        
        usuario = request.user.id
        
        ListaDeDeseo.objects.get(usuario_id=usuario,producto=producto).delete()
        
        
        ###
        ver = False
        
        
    
        return render(request,template_name="buyproduct.html",context={"product":producto,"lista":ver})




def comprafunct(request):
    
    if request.method == "POST":
        
        idproduct = Product.objects.get(id=request.POST["product"])
        
        ver = Venta.objects.filter(producto= idproduct.id,comprador=request.user.id)
        
        ver = list(ver)
        
        if ver == []:
            Venta.objects.create(vendedor_id=idproduct.belongs.id,comprador_id=request.user.id,producto_id=idproduct.id)
            
        
        
        
        return render(request,template_name="compra.html",context={"product":idproduct})



#Mostrar lista de deseos y mostrar lista de solicitudes de compra y de venta