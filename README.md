# Teste de Conversão de Áudio com o OpenAI Whisper

## Instalação e Criação do Ambiente

1 - Clonar o repositório:
```
git clone https://github.com/lucianogomes02/conversao-de-audios-teste.git
```

2 - Garantir que o ambiente virtual irá utilizar a versão 3.11 do Python:
```
poetry env use 3.11
```

3 - Criar ambiente virtual com o poetry no diretório do repositório clonado:
```
poetry shell
```

4 - Selecionar o interpretador do ambiente virtual criado na sua IDE

5 - Instalar a ferramenta de linha de comando ```ffmpeg``` na máquina:
- No Linux
```
sudo apt-get install ffmpeg
```

- No Mac
```
brew install ffmpeg
```

6 - Instalar a ferramenta de linha de comando ```llmv``` na máquina:
- No Linux
```
sudo apt-get install llmv
```

- No Mac
```
brew install llmv
```

7 - Instalar as depêndencias do projeto:
```
poetry install
```

8 - Substitua o valor da variável ```caminho_do_arquivo``` no script ```conversor-de-audio.py``` pelo caminho
do arquivo de áudio na sua maquina e rode o script.

Exemplo de execução:

![image](https://github.com/user-attachments/assets/be8574f4-5028-4e91-893f-14e977f403dc)

