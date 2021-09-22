print(f'Digite seu nome:')
nome = str(input(''))
print(f'Digite sua idade:')
idade = int(input(''))
print(f'Digite seu salário:')
salario = float(input(''))
print(f'Digite seu sexo:')
sexo = str(input(''))
print(f'Digite seu estado civíl:')
estado_civil = str(input(''))
while (True):
    if len(nome) > 3:
        if 0 <= idade <= 150:
            if salario > 0:
                if sexo == 'f' or 'm' or 'F' or 'M':
                    if estado_civil == 's' or 'S' or 'c' or 'C' or 'v' or 'V' or 'd' or 'D':
                        print(f'Todos os dados foram inseridos corretamente em nosso banco de dados')
                        break
                    else:
                        print(
                            f'O estado cívil está incorreto - Favor digite uma opção válida: (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado)')
                        estado_civil = str(input(''))
                else:
                    print(f'O sexo está incorreto - Favor digite uma opção válida: (F - Feminino, M - Masculino)')
                    sexo = str(input(''))
            else:
                print(f'O valor do salário deve ser digitado maior que zero')
                salario = float(input(''))
        else:
            print(f'O idade deve ser entre 0 e 150')
            idade = int(input(''))
    else:
        print(f'O nome deve possuir mais que 3 letras')
        nome = str(input(''))
