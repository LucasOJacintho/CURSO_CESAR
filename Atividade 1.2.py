print(f'Digite seu nome:')
nome = str(input(''))
print(f'Digite sua senha:')
senha = str(input(''))

while nome == senha:
    print(f'Aviso - os dados "nome" e a "senha" não podem ser iguais, digite sua senha novamente:')
    senha = str(input(''))

print(f'Dados cadastrados com sucesso')
