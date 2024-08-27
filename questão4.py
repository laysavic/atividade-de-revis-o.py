login = input('login: ')
senha = input('senha: ')

if login == 'admin' and senha == '123':
    print('Olá admin, seja bem-vindo')
else:
    print('login ou senha incorretos, tente novamente.')