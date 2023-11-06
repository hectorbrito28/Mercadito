from django.shortcuts import render,redirect,get_object_or_404
from . import models

from django.views.decorators.csrf import requires_csrf_token,csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
######
from .models import UserModel,Product,Mensaje
########
from django.contrib import messages
##Contraseñas
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
#
from .forms import UserRegisterForm,MensajeForm

#Imagenes
from .forms import UploadImageProduct

from django.urls import reverse


# Create your views here.



#Renderiza la interdaz del store
def storeoptions(request):
    return render(request,template_name="store.html")



#Sale cierra sesion
def exit(request):
    logout(request)
    return redirect("StoreOptions")


#Inicia sesion
def login_store(request):
    
    if request.method == "GET":
        return render(request,template_name="store_login.html",context={"form":UserRegisterForm})
    
    else:
        print(request.POST)
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        print(request.POST)
        
        if password1 == password2:
            
            ### AUTENTICAR DNI Y EMAIL MANUALMENTE,,, COLOCAR MENSAJES DE ERROR EN LOS TEMPLATES
            
            userauthenticate = authenticate(request,username= username,password=password1)
            print(userauthenticate)
            
            
            if userauthenticate is not None:
                login(request,userauthenticate)
            
                
                return redirect("Welcome")
            else:
                messages.error(request,"La cuenta no coincide o no existe en la base de datos")
                return render(request,template_name="store_login.html",context={"form":UserRegisterForm})
                
                
        else:
             messages.error(request,"Las contraseñas no coinciden")

             return render(request,template_name="store_login.html",context={"form":UserRegisterForm})
    

#Registra al usuario a la base de datos
def register_store(request):
    
    if request.method == "GET":
        
        return render(request,template_name="store_register.html",context={"form":UserRegisterForm})
    
    else:
        
        try:
            
            if request.POST["password1"] == request.POST["password2"]:
                
                UserModel.objects.create_user(username=request.POST["username"],email=request.POST["email"],dni=request.POST["dni"],password=request.POST["password1"]).save()
                    
                    
                messages.success(request,"Tu cuenta ha sido creada exitosamente")
                    
                return redirect("StoreOptions")
                
            else:
                messages.error(request,"Las contraseñas no coinciden")
                return redirect("Register")
                    
        except:
            messages.error(request,"El nombre de usuario,email o dni ya existe en la base de datos")
            return redirect("Register")
    

#Muestra configuracion de la cuenta(cambio de datos----compras)
def accountuser(request):
    return render(request,template_name="account.html")



def settingsuser(request):
    return render(request,template_name="settingsuser.html")



def sellproducts(request):
    return render(request,template_name="sellproduct.html")



def postproduct(request):
    
    
    if request.method == "GET":
        
        form = UploadImageProduct()
        
        return render(request,template_name="sellproduct.html",context={"form":form})

    else:
        
        
        
        createproduct = Product.objects.create(productimage=request.FILES["productimage"],
                                name= request.POST["name"],
                                description=request.POST["description"],
                                price = request.POST["price"],
                                category = request.POST["category"],
                                belongs_id = request.user.id
                                )
        
        messages.success(request,"Tu producto ha sido posteado")
        
        return redirect("StoreOptions")
        
        
        #form = UploadImageProduct(data=request.POST,files=request.FILES)
        
        #form.fields["belongs"].update = request.user.id
        
        
        #print(form.errors)
        
        #if form.is_valid():
            #form.save()
        



def showchats(request):
    contact = Mensaje.objects.filter(to=request.user.email)
    
    contact = Mensaje.objects.filter(to=request.user.email).distinct().values("author")
    
    lista = []
    
    for c in contact:
        lista.append(c["author"])
    
    print(lista)
    
    listausers = []
    
    for id in lista:
        usuario = Mensaje.objects.filter(author_id=id)[0]
        listausers.append(usuario)
    
    contact = listausers
    
    #histo = (contact | )
    


    return render(request,template_name="conversaciones.html",context={"contact":contact})

def showcontact(request,id):
    
    
    if request.method == "GET":
        contact = id

        
        messages_received = Mensaje.objects.filter(author=contact,to=request.user.email)
        
        contact = messages_received[0]
        
        
        messages_sent = Mensaje.objects.filter(author=request.user.id,to=contact.author.email)
        
        mensajes_history = (messages_received | messages_sent).distinct()
        
        mensajes_history = mensajes_history.order_by("datesent")
        
        print(mensajes_history)
        
    
        
        
        
        return render(request,template_name="contactchat.html",context={"mensajes":messages_received,"mensajes_enviados":messages_sent,"autor":contact.author,"me":mensajes_history})
    
    else:
        print(request.POST)
        emailto = request.POST["emailto"]
        contentsend = request.POST["ms"]
        
        Mensaje.objects.create(author=request.user,content=contentsend,to=emailto)
        
        #Redirecciona la pagina de manera recursiva
        return redirect(reverse('CONTACTt', kwargs={'id':id}))
        

def chatusers(request):
    
    if request.method == "GET":
        
        return render(request,template_name="chat.html",context={"form":MensajeForm})
    
    else:
        
        try:
            print(request.POST)
            a = get_object_or_404(UserModel,email=request.POST["to"])
            
            print(a)
        
            Mensaje.objects.create(author=request.user,content=request.POST["content"],to=request.POST["to"])
        except:
            messages.error(request,"Esa direccion de correo no existe o no esta registrada en la base de datos")
        
        
        return redirect("CHAT")
        
        

#Tarea :Colocar productos