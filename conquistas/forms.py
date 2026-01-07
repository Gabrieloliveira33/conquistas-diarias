from django import forms
from .models import Conquista



class ConquistaForm(forms.ModelForm):
    data = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'DD/MM/AAAA'}
        )
    )
    
    class Meta:
        model = Conquista
        fields = ['titulo', 'descricao', 'data', 'concluida']
