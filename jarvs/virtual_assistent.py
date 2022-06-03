import datetime
from _datetime import datetime
import os
import keyboard
import subprocess
import random
import requests
import pyjokes
import speech_recognition
import gtts
import playsound
import pywhatkit as kit
import pyttsx3

#definindo a voz
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',  'voices[1].id')

#reconhecimento de voz e fala
def ouvir():
    sr = speech_recognition
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(">>>>Ouvindo...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print(">>>>Reconhecendo...")
        intent = r.recognize_google(audio, language='pt-br')
        print(f'O que eu ouvi: {intent}\n')

    except Exception as e:
        print(e)
        fale("Desculpe, não entendi. Pode repetir?.")

        return None

    return intent.lower()

def fale(text):
    engine.say(text)
    engine.runAndWait()

def tecla_espaco():
    while True:
        try:
            if keyboard.is_pressed('space'):
                break
        except:
            break

def saldar():
    hora = datetime.now().hour
    if hora >= 6 and (hora <= 12):
        fale('Bom dia Bolacha')
        previsao_tempo()
    elif hora > 12 and (hora <= 18):
        fale("Boa tarde Bolacha")
    else:
        fale('Boa noite Bolacha')

def previsao_tempo():
    apiKey = '92e75be653b1f05e3f69e092c11f4e3e'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=guarulhos&appid={apiKey}&units=metric')
    x = response.json()
    if x["cod"] != "404":
        temperature = x['main']["temp"]
        temp = (f'A temperatura é de {temperature} graus')
        fale(temp)
    else:
        print('Desculpe, cidade não encontrada')

def abrir_camera():
    os.system('start microsoft.windows.camera:')

def escrever_txt():
    fale('O que devo escrever?')
    note_text = ouvir()
    if (note_text != None):
        f = open('textos/notes.txt', 'a')
        note = note_text + '\n\n'
        f.write(note)
        f.close()

def desligar_pc():
    desligar = fale('Fale sim, para desligar, ou não, para cancelar')
    if desligar == 'não':
        exit()
    else:
        fale("Até breve, coisa mais linda")
        os.system("shutdown /s /t 0")

#############################
def meu_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()

    print(type(ip_address["ip"]))



def youtube(video):
    kit.playonyt(video)

def pesquisar_google(query):
    kit.search(query)























