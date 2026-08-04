from django.shortcuts import render
from leads.forms import LoginForm
# Create your views here.
def login_lead(request):
    form = LoginForm()
    return render(request,'leads/login.html', {'form': form})
def cadastro_lead(request):
    return render(request,'leads/cadastro.html')
def logout_lead(request):
    return render(request,'leads/logout.html')


