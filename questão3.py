nome = input('digite seu nome:')
idade = int(input('digite sua idade:'))
if idade >= 16:
    print(f'{nome} você está apto(a) a votar')
else: 
    print(f'{nome} você não está apto(a) a votar')