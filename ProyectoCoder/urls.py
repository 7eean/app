"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from audioop import add
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="Inicio"),
    path('homepage/', home, name="Home"),
    path('about/', about, name="About"),
    #Autenticar
    path('register/', register, name="Register"),
    path('login/', iniciarSesion, name="Login"),
    path('logout/', LogoutView.as_view(template_name='autenticar/iniciarSesion.html'), name="Logout"),
    path("editarUsuario", editarUsuario, name="Editar Usuario"),
    #Reseñas
    path('reseñas/buscar', reseñaBuscador, name="Reseñas"),
    path('buscar/', buscar),
    path('agregar', addReseña, name="AddReseñas"),
    path('reseña/JeffreyDahmer', reseniaDahmer, name="RDahmer"),
    path('reseña/BetterCallSaul', reseniaSaul, name="Saul"),
    path('reseña/BreakingBad', reseniaBreaking, name="Breaking"),
    path('reseña/DevilInOhio', reseniaDevil, name="Devil"),
    path('reseña/TheWitcher', reseniaWitcher, name="Witcher"),
    path('reseña/TheBlackList', reseniaBlacklist, name="Blacklist"),
    path('reseña/Ozark', reseniaOzark, name="Ozark"),
    path('reseña/Dark', reseniaDark, name="Dark"),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)