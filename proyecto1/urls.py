"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin              #>>>> Siempre hay que importar las vistas que 
from django.urls import path                  #>>>> van a usar usadas abajo en urlpatterns.
from proyecto1.views import bienvenida, estilo_rojo, categoria_edad, random_number, conthtml    
from proyecto1.views import contplant, plantParam, plant_listas                                           


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', bienvenida),
    path('estilo/', estilo_rojo),
    path('cat_edad/<int:edad>', categoria_edad),
    path('random/', random_number),
    path('descripcion/<nombre>/<int:edad>', conthtml),
    path('index', contplant),
    path('plantparam',plantParam),
    path('plantlistas', plant_listas)
]
