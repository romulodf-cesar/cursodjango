from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(label='Nome', 
                           max_length=100,required=True)
    senha = forms.CharField(label='Senha', 
                            max_length=100,required=True,
                            widget=forms.PasswordInput())
                           
class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome', 
                           max_length=100,required=True)
    email = forms.EmailField(label='Email', 
                             max_length=100,required=True)
    senha = forms.CharField(label='Senha', 
                            max_length=100,required=True,
                            widget=forms.PasswordInput())
    