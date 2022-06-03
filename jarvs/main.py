from virtual_assistent import *

if __name__ == '__main__':
    saldar()
    previsao_tempo()
    #menu()

    while True:
        tecla_espaco()
        while True:
            intent = ouvir()
            if intent == None:
                intent
            else:
                break

        if 'abrir o google' in intent or 'abrir navegador' in intent:
            os.system('start chrome')
        elif 'txt' in intent:
            escrever_txt()
        elif 'previsão do tempo' in intent:
            previsao_tempo()

        #Contando uma piada em ingles ------------- Arrumar
        elif 'conte uma piada' in intent:
            joke = pyjokes.get_joke()
            fale(joke)
        elif 'abre câmera' in intent:
            abrir_camera()
        elif 'meu ip' in intent:
            meu_ip()
        elif 'pesquise no youtube' in intent:
            video = ouvir()
            youtube(video)
        elif 'pesquisa' in intent:
            pesquisa = ouvir()
            pesquisar_google(pesquisa)
        elif 'desligue o computador' in intent:
            desligar_pc()
        elif 'desligar' in intent:
            fale("Até breve, coisa mais linda")
            break

        else:
            fale("Não entendi, fale novamente")
