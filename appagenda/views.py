from django.shortcuts import render, redirect, get_object_or_404
from .models import Cidadao, Atendimento, Agendamento
from .forms import CidadaoForm, AgendamentoForm, AtendimentoForm
from django.contrib import messages

# Create your views here.
def home(request):
    ususario = "Francisco"
    context = {
        'usuario': ususario,
        'dtnascimento': '1975-10-04'
    }
    return render(request,'appagenda/home.html', context)

def criar_cidadao(request, pk=None):
    cidadaos = Cidadao.objects.all()
    if request.method == 'POST':
        if pk:
           #print(get_object_or_404(Cidadao,pk=pk))
           cidadao=get_object_or_404(Cidadao,pk=pk)
           form = CidadaoForm(request.POST, instance=cidadao)
           msg="Pessoa Cidadão Alterado com seucesso!"
        else:
           form = CidadaoForm(request.POST)
           msg="Pessoa cidadão cadastrado com sucesso!"
        if form.is_valid():
            form.save()
            messages.success(request, msg)
            return redirect("criar_cidadao")
        else:
            messages.error(request, "Erro ao Cadastrar!")
    else:
        if pk:
           cidadao=get_object_or_404(Cidadao,pk=pk)
           form = CidadaoForm(instance=cidadao)
        else:
           form = CidadaoForm()
    return render(request,'appagenda/formCidadao.html',
                  {"form":form,
                   "pessoas":cidadaos
                   } )


def excluir_cidadao(request, pk):
    #Criar a ação de excluir a chave pk
    cidadao = get_object_or_404(Cidadao, pk=pk)
    cidadao.delete()

    cidadaos = Cidadao.objects.all()
    form = CidadaoForm()

    return render(request,'appagenda/formCidadao.html',
                  {"form":form,
                   "pessoas":cidadaos
                   } )


def criar_atendimento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento=form.save()
            #Verificar se disponibilidade de atendimento
            atendimento = agendamento.criar_atendimento()
            if atendimento:
                return redirect('lista_atendimento')
            return redirect('listar_atendimento')  # Redireciona após salvar
    else:
        form = AgendamentoForm()

    return render(request,'appagenda/agendamento.html',{'form':form})


def realizar_atendimento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    # Verifica se já existe um atendimento vinculado
    if hasattr(agendamento, 'atendimento'):
        return redirect('realizar_atendimento', atendimento_id=agendamento.atendimento.id)

    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.cidadao = agendamento.cidadao
            atendimento.agendamento = agendamento
            atendimento.save()

            # Atualiza status do agendamento
            agendamento.status = 'R'
            agendamento.save()

            return redirect('lista_atendimento')
    else:
        # Form pré-preenchido com a descrição do agendamento
        form = AtendimentoForm(initial={
            'descricao': agendamento.descricao,
            'status': 'A'  # Em atendimento
        })

    return render(request, 'appagenda/realizar_atendimento.html', {
        'form': form,
        'agendamento': agendamento
    })

def listar_agendamento(request):
    print("1-agendamentos")
    agendamentos = Agendamento.objects.select_related('cidadao').all().order_by('-data_hora')
    print("2-agendamentos")
    return render(request, 'appagenda/lista_agendamentos.html',{'agendamentos':agendamentos})

def listar_atendimento(request):
    #atendimentos = Atendimento.objects.select_related('cidadao').all().order_by('-data_atendimento')
    atendimentos = Atendimento.objects.select_related('cidadao', 'agendamento').all().order_by('-data_atendimento')
    return render(request, 'appagenda/lista_atendimentos.html',{'atendimentos':atendimentos})
