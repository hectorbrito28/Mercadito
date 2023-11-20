from django.urls import path,include
from . import views as v2


urlpatterns = [
    path("homin/",v2.home,name="homin"),
    path("",v2.storeoptions,name="StoreOptions"),
    path("CreateAccount/",v2.register_store,name="Register"),
    path("loginuser/",v2.login_store,name="LOGINSTORE"),
    path("logout/",v2.exit,name="exit"),
    path("account/",v2.accountuser, name="ACCOUNT"),
    path("configuration/",v2.settingsuser,name="SETTINGSUSER"),
    path("Sellproduct/",v2.postproduct,name="SELLPRODUCTS"),
    path("chat/",v2.chatusers,name="CHAT"),
    path("chats/",v2.showchats,name="CHATS"),
    path("contact/<int:id>/",v2.showcontact,name="CONTACTt")
   # path("Product/",v2.postproduct,name="POSTPRODUCT")
]