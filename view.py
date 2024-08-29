from controller import ControllerCadastro, ControllerLogin

while True:
    print('-'*30)
    print('------ Sistema de Login ------')
    print('-'*30)
    print('1 - Logar')
    print('2 - Cadastrar')
    print('0 - Sair')
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        
        retorno = ControllerLogin.logar_usuario(email, senha)
        print(retorno)
        
    elif opcao == '2':
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        
        retorno = ControllerCadastro.cadastrar_usuario(nome, email, senha)
        if retorno == 1:
            print('Usuário cadastrado com sucesso.')
        else:
            print(retorno)
        
    elif opcao == '0':
        print('Sistema encerrado.')
        break
    else:
        print('Opção inválida.')