from lista_compras import *
from lista_compras_simples import *


def menu_2():
    while True:
        menu2()
        opcao = input('Insira a opção: ')
        print('-------------------------')

        if opcao == '1':
            adicionar_item()

        elif opcao == '2':
            print('Todos os itens adicionados')
            print('---------------------------------')
            mostrar_itens()
        elif opcao == '3':
            buscar_item()
        elif opcao == '4':
            remover_item()
        elif opcao == '5':
            calcular_valor()
        elif opcao == '6':
            salvar()
        elif opcao == '7':
            break

if __name__ == '__main__':
    while True:
        menu_principal()
        opcao1 = input('Insira a opção: ')
        print('---------------------------------')

        if opcao1 == '1':
            lcs()

        elif opcao1 == '2':
            print('Deseja iniciar uma lista em branco, ou carregar uma existente?')
            print('1 - Em branco\n2 - Usar Existente')
            escolha = input('Insira sua escolha: ')
            if escolha == '1':
                menu_2()
            elif escolha == '2':
                importar()
                menu_2()

        elif opcao1 == '3':
            break
