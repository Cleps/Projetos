from django import forms
from ckeditor.fields import RichTextFormField
from lista.models import Lista 
from atividade.models import Atividade
from tarefa.models import Tarefa
from ckeditor.widgets import CKEditorWidget

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['texto']
        widgets = {
            'texto': CKEditorWidget(),
        }
        

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['texto']
        widgets = {
            'texto': CKEditorWidget(),
        }
        
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['texto']
        widgets = {
            'texto': CKEditorWidget(),
        }