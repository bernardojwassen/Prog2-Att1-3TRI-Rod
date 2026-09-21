-- Alterar o nome de um usuário
UPDATE usuarios SET nome = 'João da Silva Oliveira' WHERE id_usuario = 1;

-- Alterar a disponibilidade de um livro (ex: o livro 1 agora foi emprestado/indisponível)
UPDATE livros SET disponivel = FALSE WHERE id_livro = 1;

-- Atualizar a data de devolução de um empréstimo
UPDATE emprestimos SET data_devolucao = '2026-06-30' WHERE id_emprestimo = 1;

-- Excluir um usuário (Exemplo seguro, se ele não tiver empréstimos ativos, ou se o banco permitir cascade)
DELETE FROM usuarios WHERE id_usuario = 3;

-- Excluir um livro
DELETE FROM livros WHERE id_livro = 4;