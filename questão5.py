nome = input('digite um nome: ')
disciplina = input('digite o nome da disciplina: ')
nota = float(input('digite a nota: '))

if nota < 0 or nota > 10:
    print('Nota inválida.')

else:  
    if nota >= 5.5 and nota <= 6 :
        nota = 6 
        status = 'aprovado(a)'
        print(f'{nome} está {status} em {disciplina} com nota {nota}')

    elif nota >= 6 and nota <= 10:
        status = 'aprovado(a)'
        print(f'{nome} está {status} em {disciplina} com nota {nota}')

    else:
        status = 'reprovado'
        print(f'{nome} está {status} em {disciplina} com nota {nota}')