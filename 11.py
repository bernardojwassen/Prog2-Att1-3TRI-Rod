class Produto:
    def __init__(self, codigo, nome, preco, quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade_estoque += quantidade
            print(f"Adicionadas {quantidade} unidades de {self.nome}. Estoque atual: {self.quantidade_estoque}")
        else:
            print("A quantidade a adicionar deve ser maior que zero.")

    def retirar_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            print(f"Erro: Não é possível retirar {quantidade} unidades. Estoque insuficiente ({self.quantidade_estoque} disponíveis).")
        elif quantidade <= 0:
            print("A quantidade a retirar deve ser maior que zero.")
        else:
            self.quantidade_estoque -= quantidade
            print(f"Retiradas {quantidade} unidades de {self.nome}. Estoque atual: {self.quantidade_estoque}")

    def alterar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
            print(f"O preço de {self.nome} foi alterado para R$ {self.preco:.2f}")
        else:
            print("O preço não pode ser negativo.")

    def calcular_valor_total(self):
        valor_total = self.preco * self.quantidade_estoque
        return valor_total


# Testando a classe com três objetos
print("--- TESTE DA CLASSE PRODUTO ---")
p1 = Produto("P001", "Notebook", 3500.00, 10)
p2 = Produto("P002", "Mouse", 150.00, 25)
p3 = Produto("P003", "Teclado", 250.00, 15)

# Operações de teste
p1.adicionar_estoque(5)
p1.retirar_estoque(3)
p1.retirar_estoque(20)  # Tentativa de retirar mais do que o estoque
p2.alterar_preco(130.00)

print(f"\nValor total armazenado de {p1.nome}: R$ {p1.calcular_valor_total():.2f}")
print(f"Valor total armazenado de {p2.nome}: R$ {p2.calcular_valor_total():.2f}")
print(f"Valor total armazenado de {p3.nome}: R$ {p3.calcular_valor_total():.2f}")