
from django.forms import PasswordInput, TextInput
from django import forms
from .models import Name
 
class NameForm(forms.Form):

    name = forms.CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': '', 'type': 'text'}))
    class Meta():
        model = Name
        fields = [ 'name']
      

        labels = {
            'name': ('Writer'),
        }

    #age = forms.CharField()
    """
    расчетный_счет = forms.CharField()
    наименование_банка = forms.CharField()
    фамилия_Имя_Отчество_руководителя= forms.CharField()
    """

