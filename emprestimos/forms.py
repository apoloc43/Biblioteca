from django.forms import ModelForm
from .models import Livro, Emprestimo

class LivroForm(ModelForm):
    
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'editora','quantidade','data_cadastro','autor','emprestimo']
        
        
class EmprestimoForm(ModelForm):
    
    class Meta:
        model = Emprestimo
        fields = ['codigo', 'usuario', 'data_emprestimo']        

        
            