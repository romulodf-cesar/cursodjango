from django.shortcuts import render

# Create your views here.
def login_lead(request):
    return render(request,'leads/login.html')

def cadastro_lead(request):
    return render(request,'leads/cadastro.html')
def logout_lead(request):
    return render(request,'leads/logout.html')


