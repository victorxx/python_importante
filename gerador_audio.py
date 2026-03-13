# Importar a bibliotca gTTS
from gtts import gTTS
from google.colab import files

# Texto que será transformado em áudio
texto = """

"""

# Criar o objeto TTS (usando 'pt-br' para português brasileiro)
tts = gTTS(text=texto, lang='pt-br')

# Nome do arquivo de saída
arquivo_audio = "saida.mp3"

# Salvar o arquivo de áudio
tts.save(arquivo_audio)

# Informar que o áudio foi criado
print("Áudio criado com sucesso!")

# Gerar link de download no Colab
files.download(arquivo_audio)
