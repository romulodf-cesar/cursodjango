from django.shortcuts import render, get_object_or_404  # 👈 Adicionado get_object_or_404
from motorartigos.models import Autor, Artigo, EixoTecnologia
from django.db.models import Q 

def index(request):
    # ⚡ MELHORIA DE PERFORMANCE: Adicionado select_related
    # Como você busca o nome do autor e do eixo na busca (e provavelmente nos cards),
    # o select_related traz tudo em uma única consulta ao banco, evitando o problema de "N+1 queries"
    artigos_base = Artigo.objects.filter(publicada=True).select_related('id_fk_autor', 'id_fk_eixo')
    
    eixos = EixoTecnologia.objects.all()

    termo_busca = request.GET.get('busca')
    eixo_id = request.GET.get('eixo')

    artigos_todos = artigos_base

    if eixo_id:
        artigos_todos = artigos_todos.filter(id_fk_eixo__id=eixo_id)

    if termo_busca:
        artigos_todos = artigos_todos.filter(
            Q(titulo__icontains=termo_busca) | 
            Q(texto__icontains=termo_busca) |
            Q(id_fk_autor__nome__icontains=termo_busca) |
            Q(id_fk_eixo__nome__icontains=termo_busca)
        )
    
    artigos_recentes = artigos_base.order_by('-data_publicacao')[:4]

    contexto = {
        'artigos': artigos_todos,
        'artigos_recentes': artigos_recentes,
        'eixos': eixos,                                      
        'eixo_selecionado': eixo_id,               
        'termo_busca': termo_busca                                 
    }
    return render(request, 'motorartigos/index.html', contexto)


# 🛠️ CORREÇÃO AQUI: Sua view de detalhe do artigo estava duplicada e vazia.
# Ela precisa receber o ID do artigo para buscar os dados corretos no banco e mandar pro template.
def artigo(request, artigo_id):
    # Busca o artigo pelo ID ou retorna uma página 404 caso ele não exista
    artigo_selecionado = get_object_or_404(Artigo, id=artigo_id, publicada=True)
    
    contexto = {
        'artigo': artigo_selecionado
    }
    return render(request, 'motorartigos/artigo.html', contexto)