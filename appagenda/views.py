from django.shortcuts import render, redirect
from .models import Cidadao
from .forms import CidadaoForm

# Create your views here.
def home(request):
    ususario = "Francisco"
    context = {
        'usuario': ususario,
        'dtnascimento': '1975-10-04'
    }
    return render(request,'appagenda/home.html', context)

def criar_cidadao(request):
    if request.method == 'POST':
        form = CidadaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("criar_cidadao")
    else:
        form = CidadaoForm() 
    return render(request,'appagenda/formCidadao.html',{"form":form})
