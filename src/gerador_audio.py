import os
from gtts import gTTS

def gerar_audio_narracao(texto_roteiro, arquivo_saida="output_audio.mp3"):
    print("A gerar áudio da narração com voz gratuita (Google TTS)...")
    
    # Cria o áudio em português de forma 100% gratuita
    tts = gTTS(text=texto_roteiro, lang='pt', slow=False)
    tts.save(arquivo_saida)
    
    print(f"Áudio salvo com sucesso em: {arquivo_saida}")
    return arquivo_saida

if __name__ == "__main__":
    with open("inputs/roteiro.txt", "r", encoding="utf-8") as f:
        roteiro = f.read()
    gerar_audio_narracao(roteiro)
