from django.urls import path
from . import views

app_name = 'conquistas'

urlpatterns = [
    path('', views.lista_conquistas, name='lista'),
    path('nova/', views.criar_conquista, name='criar'),
    path('editar/<int:pk>/', views.editar_conquista, name='editar'),
    path('excluir/<int:pk>/', views.excluir_conquista, name='excluir'),
]
