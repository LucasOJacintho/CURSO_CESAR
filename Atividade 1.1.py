print(f'Digite uma nota de 0 a 10')
nota = int(input(''))
while True:
    if 0 <= nota <= 10:
        print(f'A nota digitada foi: {nota}')
        break
    else:
        print(f'Digite um valor válido')
        nota = int(input(''))
