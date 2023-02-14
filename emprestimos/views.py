from django.shortcuts import render
from .models import Livro


# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros':livros})


def detalhar_livro(request,pk):
    livro = Livro.objects.get(pk=pk)
    return render(request, 'detalhar_livro.html', {'livro':livro})
    
