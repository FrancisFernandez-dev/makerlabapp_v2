from django.shortcuts import render, redirect
from .models import Model3D
from .forms import Model3DForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'biblioteca/inicio.html')


def lista_modelos(request):
    modelos = Model3D.objects.all()
    return render(request, 'biblioteca/lista_modelos.html', {'modelos': modelos})


@login_required
def agregar_modelo(request):
    if request.method == 'POST':
        form = Model3DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm()
    return render(request, 'biblioteca/agregar_modelo.html', {'form': form})


@login_required
def agregar_modelo(request):
    if request.method == 'POST':
        form = Model3DForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm()
    return render(request, 'biblioteca/agregar_modelo.html', {'form': form})

