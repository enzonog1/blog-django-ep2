from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Category, Comment, Post

SENHA_PADRAO = 'senha12345'

POSTS = [
    {
        'title': 'Primeiros passos com Django',
        'days_ago': 6,
        'categories': ['Tecnologia', 'Estudos'],
        'content': (
            '<p>O <strong>Django</strong> é um framework web em Python que já vem com '
            'administrador, ORM e sistema de templates.</p>'
            '<h2>O que eu aprendi até agora</h2>'
            '<ul>'
            '<li>Modelos descrevem as tabelas do banco de dados.</li>'
            '<li>Views recebem a requisição e devolvem uma resposta.</li>'
            '<li>Templates montam o HTML que o usuário vê.</li>'
            '</ul>'
        ),
        'comments': [
            ('maria', 'Ótimo resumo! O admin do Django economiza muito tempo.', 5),
            ('joao', 'Faltou falar das migrações, mas gostei da explicação.', 4),
            ('maria', 'Vou tentar reproduzir esse exemplo no meu computador.', 3),
        ],
    },
    {
        'title': 'Como organizo minhas semanas de prova',
        'days_ago': 3,
        'categories': ['Estudos', 'Cotidiano'],
        'content': (
            '<p>Em semana de prova, eu divido o tempo em blocos curtos e alterno '
            'as matérias.</p>'
            '<ol>'
            '<li>Resolvo exercícios primeiro.</li>'
            '<li>Releio o resumo só no final.</li>'
            '<li>Durmo bem na véspera.</li>'
            '</ol>'
        ),
        'comments': [
            ('joao', 'Resolver exercícios antes de reler o resumo funciona mesmo.', 2),
            ('maria', 'Vou adotar esse esquema na próxima prova.', 1),
        ],
    },
    {
        'title': 'Café, carona e correria: o dia a dia na faculdade',
        'days_ago': 1,
        'categories': ['Cotidiano'],
        'content': (
            '<p>Um post leve sobre o dia a dia no campus: aulas de manhã, '
            'laboratório à tarde e muito café no meio do caminho.</p>'
        ),
        'comments': [],  # este post fica sem comentários de propósito
    },
]

CATEGORIAS = [
    ('Tecnologia', 'Posts sobre programação, ferramentas e tecnologia.'),
    ('Estudos', 'Dicas e anotações sobre os estudos.'),
    ('Cotidiano', 'Histórias do dia a dia.'),
]


class Command(BaseCommand):
    help = 'Popula o banco com usuários, categorias, posts e comentários de exemplo.'

    def handle(self, *args, **options):
        User = get_user_model()
        users = {}
        for username in ('maria', 'joao'):
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(SENHA_PADRAO)
                user.save()
            users[username] = user

        categories = {}
        for name, description in CATEGORIAS:
            categories[name], _ = Category.objects.get_or_create(
                name=name, defaults={'description': description}
            )

        now = timezone.now()
        for data in POSTS:
            post, created = Post.objects.get_or_create(
                title=data['title'],
                defaults={
                    'content': data['content'],
                    'posted_at': now - timedelta(days=data['days_ago']),
                },
            )
            post.categories.add(*[categories[n] for n in data['categories']])
            if not post.comments.exists():
                for username, text, hours_ago in data['comments']:
                    Comment.objects.create(
                        post=post,
                        author=users[username],
                        text=text,
                        posted_at=now - timedelta(hours=hours_ago * 8),
                    )

        self.stdout.write(self.style.SUCCESS(
            f'Banco populado: {Post.objects.count()} posts, '
            f'{Comment.objects.count()} comentários, {Category.objects.count()} categorias.'
        ))
