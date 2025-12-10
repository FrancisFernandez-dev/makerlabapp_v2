from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Model3D, Category
from .forms import Model3DForm


def inicio(request):
    return render(request, 'biblioteca/inicio.html')


def lista_modelos(request):
    modelos = Model3D.objects.all().select_related('categoria').prefetch_related('etiquetas')
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
def editar_modelo(request, pk):
    modelo = get_object_or_404(Model3D, pk=pk)
    if request.method == 'POST':
        form = Model3DForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm(instance=modelo)
    return render(request, 'biblioteca/editar_modelo.html', {'form': form, 'modelo': modelo})


@login_required
def eliminar_modelo(request, pk):
    modelo = get_object_or_404(Model3D, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')
    return render(request, 'biblioteca/confirmar_eliminar.html', {'modelo': modelo})
