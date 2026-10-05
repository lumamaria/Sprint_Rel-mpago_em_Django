from django.urls import path
from . import views


urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),
]