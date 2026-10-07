import os
from openai import OpenAI

def gerar_audio_narracao(texto_roteiro, arquivo_saida="output_audio.mp3"):
    # Inicializa o cliente OpenAI usando a chave de ambiente configurada no GitHub Actions
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    print("Gerando áudio da narração...")
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy", # Opções: alloy, echo, fable, onyx, nova, shimmer
        input=texto_roteiro
    )
    
    response.stream_to_file(arquivo_saida)
    print(f"Áudio salvo com sucesso em: {arquivo_saida}")
    return arquivo_saida

if __name__ == "__main__":
    # Teste unitário local simulado
    with open("inputs/roteiro.txt", "r", encoding="utf-8") as f:
        roteiro = f.read()
    gerar_audio_narracao(roteiro)