from django.db import models

# Create your models here.

class Emprestimo(models.Model):
    codigo = models.CharField(max_length=15)
    usuario = models.CharField(max_length=100)
    data_emprestimo = models.DateField()
    

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    editora = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_cadastro = models.DateField()
    autor = models.CharField(max_length=100)   
    emprestimo = models.ForeignKey(Emprestimo, on_delete= models.DO_NOTHING)


