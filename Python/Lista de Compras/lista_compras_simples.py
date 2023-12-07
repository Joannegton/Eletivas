
def lcs():
    LISTA_COMPRAS_SIMPLES = []

    def menu_simples():
        print('----------------------------------')
        print('Digite 1 - Inserir Item')
        print('Digite 2 - Remover item')
        print('Digite 3 - Ver todos os Itens')
        print('Digite 4 - Salvar')
        print('Digite 5 - Sair')
        print('----------------------------------')

    def menu_0():
        print('----------------------------------------')
        print('Bem vindo a lista de compras simples, na qual que deverá\ncolocar, apenas nomes dos produtos')
        print('----------------------------------------')
        print('1 - Arquivo em Branco')
        print('2 - Carregar aquivo')

    def adc_item():
        while True:
            item = input('Insira o item a lista de compras: \nPara SAIR digite-> sair: ')
            if item != 'sair':
                LISTA_COMPRAS_SIMPLES.append(item)
                print('{} adicionado a lista'.format(item))
                print('----------------------------------')
            else:
                break
        print('----------------------------------')

    def excluir_item():
        try:
            item1 = input('Insira o item que quer remover: ')
            LISTA_COMPRAS_SIMPLES.remove(item1)
            print('{} foi removido'.format(item1))
        except:
            print('Item não existe na lista, talvez você digitou errado ou realmente não tem.')

    def export(nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                for nome in LISTA_COMPRAS_SIMPLES:
                    arquivo.write('{}\n'.format(nome))
            print('>>>>>> Lista de compras Salva com sucesso')
            print('----------------------------------')
        except:
            print('Algum erro desconhecido')
    def save():
        export('lcv.csv')

    def importando():
        try:
            with open('lcv.csv', 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    LISTA_COMPRAS_SIMPLES.append(linha.strip())
            print('-------------------------')
            print('Database carregado com sucesso')
            print('>>>>>> {} Itens carregados'.format(len(LISTA_COMPRAS_SIMPLES)))
        except FileNotFoundError:
            print('Arquivo não encontrado')
        except:
            print('Algum erro encontrado')

    def magica():
        while True:
            menu_simples()
            try:
                opcao = input('Digite uma opção: ')
            except:
                print('Insira um item valido')
            if opcao == '1':
                adc_item()
            elif opcao == '2':
                excluir_item()
            elif opcao == '3':
                print('Itens adicionados ate agora:')
                print('----------------------------------')
                for i in LISTA_COMPRAS_SIMPLES:
                    print(i)
            elif opcao == '4':
                save()
            elif opcao == '5':
                break

    menu_0()
    escolha = input('Insira uma opção: ')
    if escolha == '1':
        magica()
    elif escolha == '2':
        importando()
        magica()

