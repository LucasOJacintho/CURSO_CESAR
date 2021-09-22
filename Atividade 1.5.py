pais_a = 80000
pais_b = 200000
anos = 0

while (pais_a < pais_b):
    pais_a *= 1.03
    pais_b *= 1.015
    anos += 1

print(f'Foram necessários {anos} anos para que a população do país A ultrapassasem a população do país B.')
print(f'Em nosso levantamento temos que a população do país A é de: {int(pais_a)} habitantes e do país B é de: {int(pais_b)} habitantes.')
