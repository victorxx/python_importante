# Importar a bibliotca gTTS
from gtts import gTTS
from google.colab import files

# Texto que será transformado em áudio
texto = """
Seguro de carro cobre enchente? Entenda quando você tem direito à indenização

OPAAA ANTE DE COMEÇAR JÁ TEM UM SEGURO AUTO RESIDENCIAL ETC? NÃO NA DESCRIÇÃO DO VIDEO TEM O CONTATO TODAS AS INFORMAÇÕES

Com as fortes chuvas que têm atingido diversas regiões do país, muitos motoristas se perguntam: o seguro de carro cobre danos causados por enchentes e alagamentos? A resposta depende do tipo de cobertura contratado na apólice e das cláusulas específicas do contrato.

Especialistas em seguros alertam que a cobertura contra alagamentos está normalmente incluída no chamado seguro compreensivo (ou “total”), que protege o veículo contra colisões, incêndios, roubos e danos naturais, como enchentes, tempestades e granizo. Por outro lado, apólices que oferecem apenas cobertura contra terceiros não indenizam o proprietário em caso de danos ao próprio veículo por enchentes.

Além disso, a seguradora pode negar o pagamento se ficar comprovado que o motorista agiu com negligência, como tentar atravessar ruas alagadas ou não seguir orientações de segurança. Por isso, é essencial que os condutores leiam atentamente a apólice e conheçam os detalhes da cobertura para evitar surpresas desagradáveis.

Em casos de enchente, os especialistas recomendam registrar fotos do veículo e do local, além de acionar a seguradora imediatamente. O processo de análise da indenização pode envolver vistoria e avaliação de danos, mas essas medidas aumentam a chance de um pagamento rápido e justo.

Com o aumento de eventos climáticos extremos, entender as condições do seguro se tornou mais importante do que nunca. Motoristas que ainda não possuem seguro compreensivo podem considerar a contratação para garantir proteção contra imprevistos como enchentes.

OPAAAA O CONTATO ESTÁ A BAIXO NA DESCRIÇÃO TODO TIPO DE SEGURO
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
