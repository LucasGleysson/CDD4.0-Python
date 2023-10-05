def soma(n1, n2):
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')


def subtracao(n1, n2):
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')


def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(f'{n1} x {n2} = {resultado}')


def divisao(n1, n2):
    resultado = n1 / n2
    print(f'{n1} / {n2} = {resultado:.2f}')


def piramide_de_numeros(num):
    for i in range(num+1):
        ladeira = str(i) * i
        print(ladeira)


def ladeira_de_numeros(num):
    for i in range(num+1):
        for j in range(i):
            print(j+1, end=' ')
        print('\n')


def contador_de_vogais(texto):
    vogal = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogal:
            contador += 1
    print(contador)


def contador_de_espacos(texto):
    contador = 0
    for letra in texto:
        if letra in " ":
            contador += 1
    print(contador)


def valor_estoque_produto(produto, quantidade, valor_uni):
    valor_estoque = valor_uni * quantidade
    return valor_estoque

