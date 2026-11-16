from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Category, Comment, Post

User = get_user_model()


class Command(BaseCommand):
    help = 'Popula o banco de dados com o tema Trailer Mágico do Titio Avô.'

    def handle(self, *args, **options):
        maria, _ = User.objects.get_or_create(username='maria', defaults={'email': 'maria@example.com'})
        maria.set_password('senha12345')
        maria.save()

        joao, _ = User.objects.get_or_create(username='joao', defaults={'email': 'joao@example.com'})
        joao.set_password('senha12345')
        joao.save()

        cat_trailer, _ = Category.objects.get_or_create(
            name='Trailer Mágico',
            defaults={'description': 'Aventuras pelo espaço-tempo a bordo do Trailer Mágico.'},
        )
        cat_turma, _ = Category.objects.get_or_create(
            name='Turma do Trailer',
            defaults={'description': 'Perfis dos moradores e aliados do Titio Avô.'},
        )
        cat_missoes, _ = Category.objects.get_or_create(
            name='Missões',
            defaults={'description': 'Registros das missões e confusões resolvidas.'},
        )

        agora = timezone.now()

        p1, _ = Post.objects.get_or_create(
            title='Pochetio: O Fiel Escudeiro Mágico',
            defaults={
                'content': (
                    '<p>O <strong>Pochetio</strong> é o fiel escudeiro mágico que vive na cintura do Titio Avô. '
                    'Apesar do seu tamanho compacto, seu interior funciona como uma dimensão paralela infinita '
                    'de onde ele consegue retirar qualquer objeto imaginável — de martelos e robôs gigantes a sorvete.</p>'
                ),
            },
        )
        Post.objects.filter(pk=p1.pk).update(posted_at=agora - timedelta(days=5))
        p1.categories.set([cat_trailer, cat_turma])

        p2, _ = Post.objects.get_or_create(
            title='Sr. Gus: A Voz da Razão Jurássica',
            defaults={
                'content': (
                    '<p>O <strong>Sr. Gus</strong> é um dinossauro jurássico de mais de 100 milhões de anos que atua como '
                    'a voz da razão da equipe. Calmo, sarcástico e fã de musculação e livros, ele passa metade do tempo '
                    'tentando manter a ordem no trailer e a outra metade salvando o Titio Avô de suas próprias ideias.</p>'
                ),
            },
        )
        Post.objects.filter(pk=p2.pk).update(posted_at=agora - timedelta(days=2))
        p2.categories.set([cat_turma, cat_missoes])

        p3, _ = Post.objects.get_or_create(
            title='Steve Pizza: A Fatia Mais Maneira do Universo',
            defaults={
                'content': (
                    '<p>O <strong>Steve Pizza</strong> é uma fatia de pizza de pepperoni ultra estilosa, usuária de '
                    'óculos escuros e convencida de ser a criatura mais "maneira" do universo. Ele adora ostentar '
                    'sua popularidade e inventar bordões radicais.</p>'
                ),
            },
        )
        Post.objects.filter(pk=p3.pk).update(posted_at=agora - timedelta(hours=6))
        p3.categories.set([cat_turma])

        Comment.objects.get_or_create(
            post=p1,
            author=maria,
            text='O Pochetio sempre tira a ferramenta certa na hora do aperto!',
        )
        Comment.objects.get_or_create(
            post=p1,
            author=joao,
            text='A dimensão paralela dentro dele salva todas as missões do trailer.',
        )
        Comment.objects.get_or_create(
            post=p1,
            author=maria,
            text='Melhor companheiro de viagem pelo espaço-tempo!',
        )

        Comment.objects.get_or_create(
            post=p2,
            author=joao,
            text='O Sr. Gus é o único que mantém a calma quando o plano foge do controle.',
        )
        Comment.objects.get_or_create(
            post=p2,
            author=maria,
            text='Fã de musculação, livros e paciência infinita com o Steve Pizza.',
        )

        self.stdout.write(self.style.SUCCESS('Banco populado com o tema Trailer Mágico do Titio Avô!'))