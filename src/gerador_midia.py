import os
import requests
from PIL import Image, ImageDraw, ImageFont

def criar_imagem_fundo(titulo_episodio="Episódio 01", arquivo_saida="output_bg.png"):
    print("A descarregar imagem de fundo vertical aleatória...")
    
    # URL de imagens verticais de alta qualidade 100% gratuita (Picsum Photos)
    url = "https://picsum.photos/1080/1920"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            with open(arquivo_saida, 'wb') as f:
                f.write(response.content)
            
            # Aplica uma camada escura semi-transparente por cima para destacar o texto do vídeo
            img = Image.open(arquivo_saida).convert("RGBA")
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 140)) # Escurece o fundo
            img_combinada = Image.alpha_composite(img, overlay).convert("RGB")
            img_combinada.save(arquivo_saida)
            
            print(f"Imagem de fundo aplicada com sucesso: {arquivo_saida}")
            return arquivo_saida
    except Exception as e:
        print(f"Aviso ao obter imagem da web: {e}. A usar fundo de segurança.")
        
    # Fallback caso ocorra algum problema de rede: cria um fundo escuro elegante
    largura, altura = 1080, 1920
    imagem = Image.new("RGB", (largura, altura), color=(15, 15, 25))
    imagem.save(arquivo_saida)
    return arquivo_saida

if __name__ == "__main__":
    criar_imagem_fundo()
