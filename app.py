'''
Complete  o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agencia, conta e saldo. E ai o usuário vai poder escolher se deseja fazer saque, depósito ou sair do programa.
'''

import modulo

if __name__ == "__main__":
        
    print('Seja bem vindo ao seu banco digital')
    print('\n=====menu=====')
    print('1 - Cadastrar usuário')
    print('2 - Deletar usuário')
    print('3 - Entrar no aplicativo')
    print('4 - Sair')
    print('\n')

    while True:
        opcao = input('Escolha uma opção: ')
        match opcao:
            case '1':
                nome = input('Digite o nome do usuário: ')
                modulo.cadastrar_usuario(nome)
                
            case '2':
                nome = input('Digite o nome do usuário que deseja deletar: ')
                modulo.deletar_usuario(nome)
                
            case '3':
                nome = input('Digite o seu nome: ')

                if modulo.entrar(nome):
                    while True:
                        print("\n=== MENU ===")
                        print("1. Depositar")
                        print("2. Sacar")
                        print("3. Sair")

                        opcao_usr = input('Escolha uma opção: ')

                        if opcao_usr == '1':
                            valor = float(input('Digite o valor a ser depositado: '))
                            modulo.depositar(nome, valor)
                        elif opcao_usr == '2':
                            valor = float(input('Informe o valor a ser sacado: '))
                            modulo.sacar(nome, valor)
                        elif opcao_usr == '3':
                            break
                        else:
                            print('Opção inválida')
                else:
                    print('Usuário inválido')
                break
            case '4':
                print("Obrigado por usar nosso banco digital. Volte sempre!")
                exit()
            case _:
                print('Opção inválida')
