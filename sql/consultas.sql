-- Consulta 1: Todos os posts, ordenados pela data (mais recente primeiro)
SELECT *
FROM blog_post
ORDER BY posted_at DESC;

-- Consulta 2: Todos os comentários de um post (ex: post_id = 1)
SELECT *
FROM blog_comment
WHERE post_id = 1;

-- Consulta 3: Comentários de um post com colunas do comentário (exceto post_id),
-- título do post e data de publicação renomeada para post_date
SELECT c.id, c.author_id, c.text, c.posted_at,
       p.title, p.posted_at AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE p.id = 1;

-- Consulta 4: Todos os posts pertencentes a uma categoria, incluindo colunas da categoria e do post
SELECT c.id AS category_id, c.name, c.description,
       p.id AS post_id, p.title, p.content, p.posted_at
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
JOIN blog_post AS p ON p.id = pc.post_id
WHERE c.name = 'Trailer Mágico';

-- Consulta 5: Todas as categorias que possuem dois ou mais posts
SELECT c.id, c.name, c.description, COUNT(pc.post_id) AS total_posts
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
GROUP BY c.id, c.name, c.description
HAVING COUNT(pc.post_id) >= 2;