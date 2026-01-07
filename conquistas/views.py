from django.shortcuts import render, redirect, get_object_or_404
from .models import Conquista
from .forms import ConquistaForm
from django.contrib.auth.decorators import login_required


@login_required
def lista_conquistas(request):
    conquistas = Conquista.objects.all()
    return render(request, 'conquistas/lista.html', {'conquistas': conquistas})

@login_required
def criar_conquista(request):
    if request.method == 'POST':
        form = ConquistaForm(request.POST)
        if form.is_valid():
            conquista = form.save(commit=False)
            conquista.usuario = request.user
            conquista.save()
            return redirect('conquistas:lista')
    else:
        form = ConquistaForm()
    return render(request, 'conquistas/form.html', {'form': form})

@login_required
def editar_conquista(request, pk):
    conquista = get_object_or_404(Conquista, pk=pk)
    form = ConquistaForm(request.POST or None, instance=conquista)
    if form.is_valid():
        form.save()
        return redirect('conquistas:lista')
    return render(request, 'conquistas/form.html', {'form': form})

@login_required
def excluir_conquista(request, pk):
    conquista = get_object_or_404(Conquista, pk=pk)
    if request.method == 'POST':
        conquista.delete()
        return redirect('conquistas:lista')
    return render(request, 'conquistas/confirmar_exclusao.html', {'conquista': conquista})
