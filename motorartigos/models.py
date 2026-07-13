from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    biografia = models.TextField(verbose_name='Biografia')
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=60, verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'eixo'
        verbose_name = 'Eixo de Tecnologia'
        verbose_name_plural = 'Eixos de Tecnologia'


class Artigo(models.Model):

    titulo = models.CharField(        
        max_length=200,
        verbose_name='Título',
        default='Sem título'
    )
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    # 2. Adicione este campo virtual. Ele lerá a sua 'foto' e criará o thumbnail em cache
    foto_card = ImageSpecField(
        source='foto',
        processors=[ResizeToFill(400, 250)], # Redimensiona e corta para encaixar no card
        format='JPEG',
        options={'quality': 85}
    )
    publicada = models.BooleanField(default=False)
    TAG_NIVEL = [
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    ]

    nivel = models.CharField(
        max_length=1,           
        choices=TAG_NIVEL,
        default='B',            
        verbose_name='Nível'
    )
    texto = HTMLField(verbose_name='Texto')
    data_publicacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Publicação'
    )
    id_fk_eixo = models.ForeignKey(
        EixoTecnologia,
        on_delete=models.CASCADE,
        db_column='id_fk_eixo',
        verbose_name='Eixo',        
        related_name='artigos'
    )
    id_fk_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_fk_autor',
        verbose_name='Autor',       
        related_name='artigos'
    )

    def __str__(self):
        return f"Artigo {self.id} – {self.id_fk_autor.nome}"  # 👈 mais legível

    class Meta:
        db_table = 'artigo'
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']  
    # Adicione este método dentro da classe Artigo no seu models.py:
    def get_absolute_url(self):
       return reverse('detalhe_artigo', args=[self.id])
