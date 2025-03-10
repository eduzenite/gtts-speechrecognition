# Descrição
Na minha solução, utilizei a biblioteca gTTS para converter textos em áudio e a SpeechRecognition para capturar e transcrever a fala do usuário.
Criei um dicionário contendo todas as frases utilizadas no atendimento, incluindo:
- Opções do menu de atendimento.
- Mensagens de confirmação para garantir que uma opção foi selecionada corretamente.
- Mensagem de despedida para quando o cliente optar por sair.
- Mensagem de erro caso o sistema não compreenda a entrada do usuário.
Para otimizar o processo, implementei um loop que percorre todas as frases do dicionário, gera os arquivos de áudio correspondentes e os armazena na pasta “arquivos/”.
Além disso, desenvolvi:
- Uma função para tocar os áudios armazenados
- Uma função para capturar o áudio da fala do usuário, transcrevê-lo e retornar o texto correspondente.
  - Dentro dessa função, implementei duas exceções:
    - sr.UnknownValueError: Caso o sistema não consiga entender o que foi falado.
    - sr.RequestError: Caso ocorra um erro na comunicação com o serviço de reconhecimento de voz.
Por fim, criei um loop principal que:
- Apresenta as opções do menu ao cliente
- Captura a resposta do usuário via comando de voz
- Toca a mensagem de confirmação correspondente
- Permite que o usuário continue interagindo ou encerre o atendimento
# Execução
Para executar o código será preciso instalar as bibliotecas:
```console
pip install gtts
pip install SpeechRecognition
```
# Arquivos
Vídeo: https://youtu.be/63ZEGwv77jk
