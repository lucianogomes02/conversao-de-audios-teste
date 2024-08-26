import whisper


def converter_audio_em_texto(caminho_do_arquivo: str) -> str:
    modelo = whisper.load_model("base")
    transcricao = modelo.transcribe(caminho_do_arquivo)
    return transcricao["text"]


if __name__ == '__main__':
    print(converter_audio_em_texto("/Users/lucianogomes/Documents/Audios Teste/teste-arthur.m4a"))
