from tecateca import valor_estoque_produto

produto = input("Digite o nome do produto: ")
qnt = int(input("Digite a quantidade: "))
val_unit = float(input("Digite o valor unitário: "))

valor_estoque = valor_estoque_produto(produto, qnt, val_unit)

print(f'PRODUTO: {produto}')
print(f'Valor Unitário: RS {val_unit:.2f}')
print(f'Valor Total: RS {valor_estoque:.2f}')

