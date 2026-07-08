!pip install gtts -q

from gtts import gTTS
from IPython.display import Audio
from google.colab import files

# Texto que será transformado em áudio
texto = """
# Seguro passa a olhar mais para a vida: proteção financeira ganha espaço nas novas estratégias do setor

O mercado de seguros está passando por uma transformação importante. Cada vez mais, as empresas deixam de apresentar o seguro apenas como uma proteção para situações inesperadas e passam a destacar soluções voltadas para a segurança financeira, o planejamento familiar e o cuidado durante diferentes fases da vida.

A chamada proteção em vida vem ganhando força ao oferecer benefícios que podem ser utilizados enquanto o segurado está vivo, como apoio financeiro em momentos de dificuldade, cobertura para doenças graves, planejamento de futuro e recursos para manter a estabilidade da família.

Essa mudança acompanha um novo comportamento dos consumidores, que buscam produtos mais completos e alinhados às suas necessidades reais. Em vez de contratar um seguro pensando somente em um evento extremo, muitas pessoas passaram a enxergar a contratação como uma ferramenta de organização financeira e prevenção.

O setor também aposta em produtos mais personalizados, com coberturas adaptadas ao perfil de cada cliente. A tecnologia tem contribuído para essa evolução, tornando processos de contratação mais simples e permitindo uma relação mais próxima entre seguradoras e consumidores.

Especialistas apontam que a tendência é que o seguro continue ampliando seu papel na sociedade, passando de uma solução tradicional de indenização para um instrumento de proteção contínua, capaz de oferecer suporte em diferentes momentos da trajetória pessoal e profissional.

Com essa nova visão, o conceito de seguro deixa de estar ligado apenas ao risco e passa a representar planejamento, tranquilidade e qualidade de vida.

"""

# Criar áudio
arquivo = "audio.mp3"

voz = gTTS(
    text=texto,
    lang="pt-br",
    slow=False
)

# Salvar arquivo
voz.save(arquivo)

# Reproduzir no Colab
display(Audio(arquivo))

# Baixar o arquivo
files.download(arquivo)
