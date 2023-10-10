from tecateca import calc_media, status_media_aprovacao

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = calc_media(n1, n2)

print(f'A média é {media} e ele esta ', end=' ')
status_media_aprovacao(media)

