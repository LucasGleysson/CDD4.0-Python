from tecateca import calc_media, situacao_nota

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = calc_media(n1, n2)

print(f'A média é {media} e ele esta ', end=' ')
situacao_nota(media)

