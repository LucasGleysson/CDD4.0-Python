lista_numeros = [1,2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
nova_lista = [0] * len(lista_numeros)
lista_temp = [0]
tamanho = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] == 0:
        continue
    if lista_numeros[i] not in nova_lista:
        nova_lista[i] = lista_numeros[i]
        tamanho = 0
nova_nova_lista = [0] * tamanho
print(nova_lista)
