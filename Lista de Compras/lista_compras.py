
LISTA_COMPRAS = {'massa de tomate':
                     {'valor': 1, 'quantidade': 10}
}

def adicionar_item():
        while True:
            nome = input('Insira o nome do item: \nPara SAIR insira-> sair')
            if nome == 'sair':
                print('-------------------------')
                break
            else:
                valor = float(input('Insira o valor do item: '))
                quant = int(input('Insira a quantidade do item: '))

                LISTA_COMPRAS[nome] = {
                    'valor': valor,
                    'quantidade': quant
                }
                print('Você adicionou {} {} no valor de {} a lista de compras'.format(quant, nome, valor))
                print('---------------------------------')

def remover_item():
    nome = input('Insira o nome do item a ser Removido: ')
    LISTA_COMPRAS.pop(nome)
    print('>>>>> item {}, foi excluido com sucesso'.format(nome))

def mostrar_itens():
    if LISTA_COMPRAS:
        for item in LISTA_COMPRAS:
            print(item)

        print('-------------------------')

def buscar_item():
    try:
        nome = input('Insira o nome do item: ')
        valor = LISTA_COMPRAS[nome]['valor']
        quantid = LISTA_COMPRAS[nome]['quantidade']
        print('Nome:', nome)
        print('valor:', valor)
        print('Quantidade:', quantid)
        resultado = (valor * quantid)

        print('Total do {}: '.format(nome), resultado)
        print('-------------------------')
    except KeyError:
        print('Item não existe.')
    except Exception:
        print('>>>>> Algum erro inexperado ocorreu')


def calcular_valor():
    pass
    '''
    a = LISTA_COMPRAS.values()
    b = list(a)
    soma = 0
    for item in b:
        c = item.values()
        d = (sum(c))
        soma += d
        if soma:
            print(soma)
'''
def exportar(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for nome in LISTA_COMPRAS:
                valor = LISTA_COMPRAS[nome]['valor']
                quanti = LISTA_COMPRAS[nome]['quantidade']

                arquivo.write('{},{},{}\n'.format(nome, valor, quanti))
        print('>>>>>> Lista de compras Salva com sucesso')
    except:
        print('Algum erro ocorreu')
def salvar():
    exportar('lista_supermecado.csv')

def importar():
    try:
        with open('lista_supermecado.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))

                nome = detalhes[0]
                valor = detalhes[1]
                quant = detalhes[2]

                LISTA_COMPRAS[nome] = {
                    'valor': valor,
                    'quantidade': quant
                }

        print('Database carregado com sucesso')
        print('>>>>>> {} Itens carregados'.format(len(LISTA_COMPRAS)))
        print('---------------------------------')

    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Algum erro aconteceu')
        print(error)



def menu_principal():
    print('1 - Lista de compras')
    print('2 - No Supermerdado')
    print('3 - Sair')

def menu2():
    print('1 - Adicionar item')
    print('2 - Ver todos itens')
    print('3 - Conferir item')
    print('4 - Remover item')
    print('5 - Mostrar Valor total da compra')
    print('6 - Salvar')
    print('7 - Sair')

