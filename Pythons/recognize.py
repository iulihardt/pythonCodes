import speech_recognition as sr


#Funcao que converte fala em texto.
def voz_to_text():
    microfone = sr.Recognizer() #identifica o microfone
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) #aplica módulo de reduçao de ruido
        print("Diga alguma coisa: ") #solicita para falar e ouvir o microfone
        audio = microfone.listen(source)
    
    try:
        frase = microfone.recognize_google(audio,language="pt-BR") #transcreve o som para Portugues BR
        print(frase) #printa na tela a frase

    except sr.UnknownValueError:
        print("Nao rolou") #ou retorna erro


    return frase
voz_to_text()

#proximos passos
"""
1) ler arquivos .mp3, .mp4 ...
2) Converter o audio do arquivo em .csv
3) funçao loop numa pasta com N audios 
4) aplicar closterizaçao de textos e ML no csv ou APLICAR num BI
"""