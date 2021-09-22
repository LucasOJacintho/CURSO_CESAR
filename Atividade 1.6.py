print(f'Digite a população do País A:')
pais_a = int(input(''))
print(f'Digite a população do País B:')
pais_b = int(input(''))
print(f'Digite a taxa de crescimento de 0 a 100 do País A:')
taxa_a = float(input(''))
print(f'Digite a taxa de crescimento de 0 a 100 do País B:')
taxa_b = float(input(''))
popPais_a = pais_a
popPais_b = pais_b

anos = 0
verificador = 0

while (True):
    if pais_a < 0:
        print(f'Digite a população do País A corretamente - O valor deverá ser maior que 0:')
        pais_a = int(input(''))
        verificador += 1
    if pais_b < 0 or pais_b < pais_a:
        print(f'Digite a população do País B corretamente - O valor deverá ser maior que 0 - '
              f'Para que seja possível a análise não retorne um loop infinito informe uma população superior ao do País A:')
        pais_b = int(input(''))
        verificador += 1
    if not (0 < taxa_a <= 100):
        print(
            f'Digite a taxa de crescimento do País A corretamente - O valor deverá ser maior que 0 e maior ou igual a 100:')
        taxa_a = float(input(''))
        verificador += 1
    if 0 > taxa_b > 100 or taxa_a <= taxa_b:
        print(
            f'Digite a taxa de crescimento do País B corretamente - O valor deverá ser maior ou igual a 0 e maior ou igual a 100 - '
            f'para que seja possível a análise não retorne um loop infinito informe uma taxa de crescimento inferior ao do País A:')
        taxa_b = float(input(''))
        verificador += 1

    while (popPais_a < popPais_b) and verificador == 0:
        popPais_a = popPais_a * (taxa_a / 100 + 1)
        popPais_b = popPais_b * (taxa_b / 100 + 1)
        anos += 1

    if verificador == 0:
        print(f'----------------------Resumo-------------------------')
        print(f'|          Dados          |   País A   |   País B   |')
        print(f'|    Populacao inicial    |    {int(pais_a)}    |    {int(pais_b)}    |')
        print(f'|   Taxa de crescimento   |    {taxa_a}%    |    {taxa_b}%    |')
        print(f'|    Anos necessários     |            {anos}           |')
        print(f'|  População atualizada   |    {int(popPais_a)}   |   {int(popPais_b)}    |')

    if verificador == 0:
        break
    else:
        verificador = 0
