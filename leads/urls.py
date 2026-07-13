from django.urls import path
from leads.views import login_lead,cadastro_lead,logout_lead

urlpatterns = [
    path('login',login_lead,name='login'),
    path('cadastro',cadastro_lead,name='cadastro'),
    path('logout',logout_lead,name='logout'),    
]

