from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('modelos/', views.lista_modelos, name='lista_modelos'),
    path('modelos/agregar/', views.agregar_modelo, name='agregar_modelo'),
    
]
