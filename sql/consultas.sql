

-- Query 1: Todos os posts, do mais recente para o mais antigo
SELECT id, title, posted_at, content
FROM blog_post
ORDER BY posted_at DESC;

-- Query 2: Todos os comentários de um post (o post com id = 1)
SELECT *
FROM blog_comment
WHERE post_id = 1;

-- Query 3: Comentários de um post com título e data do post (post_date), sem a coluna post_id
SELECT c.id, c.author_id, c.text, c.posted_at,
       p.title, p.posted_at AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE p.id = 1;

-- Query 4: Todos os posts de uma categoria (Estudos), com colunas da categoria e do post
SELECT c.id AS category_id, c.name, c.description,
       p.id AS post_id, p.title, p.content, p.posted_at
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
JOIN blog_post AS p ON p.id = pc.post_id
WHERE c.name = 'Trailer Mágico';

-- Query 5: Categorias que possuem dois ou mais posts
SELECT c.id, c.name, c.description, COUNT(pc.post_id) AS total_posts
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
GROUP BY c.id, c.name, c.description
HAVING COUNT(pc.post_id) >= 2;

