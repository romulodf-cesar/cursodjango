from django.urls import path
from motorartigos.views import index,artigo

urlpatterns = [
    path('',index,name='index'),
    path('artigo/',artigo,name='artigo'),
    path('artigo/<int:artigo_id>/', artigo, name='detalhe_artigo'),
 ]