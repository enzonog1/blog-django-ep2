# Meu Blog (Django)

Blog dinâmico feito com Django: CRUD de posts, comentários e categorias.

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # para entrar em /admin/
python manage.py seed            # popula 3 posts, 3 categorias e comentários de exemplo
python manage.py runserver
```

Abra http://127.0.0.1:8000/. Usuários de teste criados pelo `seed`: `maria` e `joao`
(senha `senha12345`). É preciso estar logado para comentar.

## Rotas

| URL                              | Nome            | O que faz                         |
|----------------------------------|-----------------|-----------------------------------|
| `/`                              | post_list       | lista os posts                    |
| `/posts/new/`                    | post_create     | cria um post                      |
| `/posts/<id>/`                   | post_detail     | mostra o post, comentários e categorias |
| `/posts/<id>/edit/`              | post_update     | edita o post                      |
| `/posts/<id>/delete/`            | post_delete     | confirma e remove o post          |
| `/posts/<id>/comments/new/`      | comment_create  | cria um comentário (exige login)  |
| `/categories/`                   | category_list   | lista as categorias               |
| `/categories/<id>/`              | category_detail | posts de uma categoria            |

## Histórico do Git

As três versões das views estão nos commits marcados com as tags `v1-sem-forms`,
`v2-com-forms` e `v3-generic-views`. Os branches `comments` e `categories`
foram mesclados em `main`.
