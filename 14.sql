-- Cadastrando Autores
INSERT INTO autores (nome, nacionalidade) VALUES ('Machado de Assis', 'Brasileira');
INSERT INTO autores (nome, nacionalidade) VALUES ('J.K. Rowling', 'Britânica');
INSERT INTO autores (nome, nacionalidade) VALUES ('George Orwell', 'Britânica');

-- Cadastrando Livros (5 livros)
INSERT INTO livros (titulo, id_autor, ano_publicacao, disponivel) VALUES ('Dom Casmurro', 1, 1899, TRUE);
INSERT INTO livros (titulo, id_autor, ano_publicacao, disponivel) VALUES ('Memórias Póstumas de Brás Cubas', 1, 1881, FALSE);
INSERT INTO livros (titulo, id_autor, ano_publicacao, disponivel) VALUES ('Harry Potter e a Pedra Filosofal', 2, 1997, TRUE);
INSERT INTO livros (titulo, id_autor, ano_publicacao, disponivel) VALUES ('Harry Potter e a Câmara Secreta', 2, 1998, TRUE);
INSERT INTO livros (titulo, id_autor, ano_publicacao, disponivel) VALUES ('1984', 3, 1949, FALSE);

-- Cadastrando Usuários (3 usuários)
INSERT INTO usuarios (nome, email, telefone) VALUES ('João Oliveira', 'joao@email.com', '11999998888');
INSERT INTO usuarios (nome, email, telefone) VALUES ('Maria Santos', 'maria@email.com', '11988887777');
INSERT INTO usuarios (nome, email, telefone) VALUES ('Pedro Lima', 'pedro@email.com', '11977776666');

-- Cadastrando Empréstimos (3 empréstimos)
INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (2, 1, '2026-06-01', '2026-06-15');
INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (5, 2, '2026-06-05', '2026-06-20');
INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (1, 3, '2026-06-10', '2026-06-25');

-- 1. Listar todos os livros
SELECT * FROM livros;

-- 2. Mostrar somente título e autor (fazendo JOIN com a tabela autores)
SELECT livros.titulo, autores.nome AS autor 
FROM livros 
JOIN autores ON livros.id_autor = autores.id_autor;

-- 3. Buscar livros de determinado autor (Ex: J.K. Rowling)
SELECT livros.titulo 
FROM livros 
JOIN autores ON livros.id_autor = autores.id_autor 
WHERE autores.nome = 'J.K. Rowling';

-- 4. Mostrar os livros ordenados alfabeticamente
SELECT * FROM livros ORDER BY titulo ASC;

-- 5. Mostrar apenas livros disponíveis
SELECT * FROM livros WHERE disponivel = TRUE;