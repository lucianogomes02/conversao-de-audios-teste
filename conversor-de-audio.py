import whisper


def converter_audio_em_texto(caminho_do_arquivo: str) -> str:
    modelo = whisper.load_model("base")
    transcricao = modelo.transcribe(caminho_do_arquivo)
    return transcricao["text"]


if __name__ == '__main__':
    caminho_do_arquivo = "COLOQUE O CAMINHO DO AUDIO AQUI"
    print(converter_audio_em_texto(caminho_do_arquivo))
