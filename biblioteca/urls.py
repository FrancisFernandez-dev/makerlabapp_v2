from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('modelos/', views.lista_modelos, name='lista_modelos'),
    path('modelos/agregar/', views.agregar_modelo, name='agregar_modelo'),
    path('modelos/<int:pk>/editar/', views.editar_modelo, name='editar_modelo'),
    path('modelos/<int:pk>/eliminar/', views.eliminar_modelo, name='eliminar_modelo'),


]
