from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

# Create your views here.

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/lista_projetos.html', {'projetos': projetos})


def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'core/cadastra_projetos.html', {'form': form})

def editar_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/edita_projeto.html', {'form': form})


def excluir_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')

    return render(request, 'core/exclui_projeto.html', {'projeto': projeto})