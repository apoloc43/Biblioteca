from django.urls import  path
from .views import listar_livros,detalhar_livro


urlpatterns = [
    
    path('listar_livros/', listar_livros,name='listar_livros'),
    path('detalhar_livro/<int:pk>', detalhar_livro,name='detalhar_livro'),
    
    
    
]
