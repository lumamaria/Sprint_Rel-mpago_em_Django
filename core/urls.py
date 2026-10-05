from django.urls import path
from . import views


urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/excluir/', views.excluir_projeto, name='excluir_projeto'),
]