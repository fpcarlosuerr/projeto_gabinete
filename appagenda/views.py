from django.shortcuts import render, redirect
from .models import Cidadao
from .forms import CidadaoForm
from django.contrib import messages

# Create your views here.
def home(request):
    ususario = "Francisco"
    context = {
        'usuario': ususario,
        'dtnascimento': '1975-10-04'
    }
    return render(request,'appagenda/home.html', context)

def criar_cidadao(request):
    cidadaos = Cidadao.objects.all()
    if request.method == 'POST':
        form = CidadaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoa cidadão cadastrado com sucesso!")
            return redirect("criar_cidadao")
        else:
            messages.error(request, "Erro ao Cadastrar!")
    else:
        form = CidadaoForm() 
    return render(request,'appagenda/formCidadao.html',
                  {"form":form,
                   "pessoas":cidadaos
                   } )

def criar_agendamento(request):

    return render(request,'appagenda/agendamento.html')