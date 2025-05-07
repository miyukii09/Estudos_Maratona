N, H = map(int, input().split())
alturas_minimas = list(map(int, input().split()))

contador = 0
for altura in alturas_minimas:
    if H >= altura:
        contador += 1

print(contador)
