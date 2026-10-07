import os
import subprocess
from gerador_audio import gerar_audio_narracao
from gerador_midia import criar_imagem_fundo

def executar_pipeline():
    caminho_roteiro = "inputs/roteiro.txt"
    if not os.path.exists(caminho_roteiro):
        raise FileNotFoundError(f"Arquivo de roteiro não encontrado em {caminho_roteiro}")
        
    with open(caminho_roteiro, "r", encoding="utf-8") as f:
        roteiro = f.read().strip()
        
    print(f"Roteiro carregado ({len(roteiro)} caracteres).")
    
    # Gera os assets usando ferramentas gratuitas
    arquivo_audio = gerar_audio_narracao(roteiro, "temp_audio.mp3")
    
    titulo_visual = roteiro.split("\n")[0][:30] + "..."
    arquivo_imagem = criar_imagem_fundo(titulo_visual, "temp_bg.png")
    
    # Monta o vídeo final utilizando FFmpeg
    saida_video = "output.mp4"
    comando = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", arquivo_imagem,
        "-i", arquivo_audio,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        saida_video
    ]
    
    print("A renderizar vídeo final via FFmpeg...")
    subprocess.run(comando, check=True)
    print(f"Vídeo gerado com sucesso: {saida_video}")
    
    for temp in [arquivo_audio, arquivo_imagem]:
        if os.path.exists(temp):
            os.remove(temp)

if __name__ == "__main__":
    executar_pipeline()
