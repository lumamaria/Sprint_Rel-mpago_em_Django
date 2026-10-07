from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('projetos/cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/excluir/', views.excluir_projeto, name='excluir_projeto'),

    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/cadastrar/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('tarefas/<int:id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
]