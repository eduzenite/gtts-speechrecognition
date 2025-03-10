from gtts import gTTS
import os
import speech_recognition as sr

# Função para gerar áudio a partir de um texto e salvar em um arquivo
def gerar_audio(texto, nome_arquivo):
    tts = gTTS(texto, lang="pt")
    tts.save(nome_arquivo)

# Gera as frases de atendimento e as salva em arquivos de áudio
frases = {
    "saudacao": "Bem-vindo à QuantumFinance. Por favor, escolha uma das seguintes opções:",
    "opcao1": "1. Diga conta para consulta ao saldo da conta.",
    "opcao2": "2. Diga compra para simulação de compra internacional.",
    "opcao3": "3. Diga atendente para falar com um atendente.",
    "opcao4": "4. Diga sair para sair do atendimento.",
    "confirmacao1a": "Você escolheu Consulta ao saldo da conta.",
    "confirmacao1b": "Seu saldo atual é de R$ 1.500,00.",
    "confirmacao2a": "Você escolheu Simulação de compra internacional.",
    "confirmacao2b": "O valor da compra é de R$ 500,00.",
    "confirmacao3a": "Você escolheu Falar com um atendente.",
    "confirmacao3b": "Por favor, aguarde um momento enquanto transferimos sua ligação.",
    "confirmacao4": "Você escolheu Sair do atendimento. Obrigado e até logo!",
    "erro": "Desculpe, não entendi sua escolha. Por favor, tente novamente."
}

# Gera os arquivos de áudio para cada frase
for chave, texto in frases.items():
    gerar_audio(texto, f"arquivos/{chave}.mp3")
    print(f"Arquivo {chave}.mp3 gerado com sucesso.")

# Função para tocar um arquivo de áudio
def tocar_audio(nome_arquivo):
    print(f"Tocando arquivos/{nome_arquivo}.mp3")
    os.system(f"afplay arquivos/{nome_arquivo}.mp3")

# Função para capturar áudio do usuário e transcrever
def capturar_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            gerar_audio(f"Você disse: {texto}", "arquivos/selecao.mp3")
            tocar_audio("selecao")
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError:
            print("Erro ao conectar ao serviço de reconhecimento de fala.")
            return None

# Loop de atendimento
while True:
    # Toca as opções de atendimento
    tocar_audio("saudacao")
    tocar_audio("opcao1")
    tocar_audio("opcao2")
    tocar_audio("opcao3")
    tocar_audio("opcao4")

    # Captura a escolha do usuário
    escolha = capturar_audio()

    # Verifica a escolha do usuário e toca a confirmação correspondente
    if escolha:
        if "consulta" in escolha or "saldo" in escolha or "um" in escolha:
            tocar_audio("confirmacao1a")
            tocar_audio("confirmacao1b")
        elif "simulação" in escolha or "compra" in escolha or "internacional" in escolha or "dois" in escolha:
            tocar_audio("confirmacao2a")
            tocar_audio("confirmacao2b")
        elif "falar" in escolha or "atendente" in escolha or "três" in escolha:
            tocar_audio("confirmacao3a")
            tocar_audio("confirmacao3b")
        elif "sair" in escolha or "quatro" in escolha:
            tocar_audio("confirmacao4")
            break
        else:
            tocar_audio("erro")
    else:
        tocar_audio("erro")