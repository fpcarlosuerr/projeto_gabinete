from django.urls import path
from . import views

#rotas da aplicação appagenda
urlpatterns = [
    path('',views.home, name="home"),
    path('criar_cidadao',views.criar_cidadao,name='criar_cidadao'),
]
