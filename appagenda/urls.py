from django.urls import path
from . import views

#rotas da aplicação appagenda
urlpatterns = [
    path('',views.home, name="home"),
    path('criar_cidadao',views.criar_cidadao,name='criar_cidadao'),
    path('criar_cidadao/<int:pk>',views.criar_cidadao,name='editar_cidadao'),
    path('exluir_cidadao/<int:pk>',views.excluir_cidadao,name='excluir_cidadao'),
    path('agendamento/',views.criar_atendimento,name='agendar_atendimento'),
    path('agendamento/lista',views.listar_agendamento,name='lista_agendamento'),
    path('atendimento/lista',views.listar_atendimento,name='lista_atendimento'),
    path('atendimento/realizar/<int:agendamento_id>/', views.realizar_atendimento, name='realizar_atendimento'),


]
