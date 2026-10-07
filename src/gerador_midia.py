import os
from PIL import Image, ImageDraw, ImageFont

def criar_imagem_fundo(titulo_episodio="Episódio 01", arquivo_saida="output_bg.png"):
    # Cria uma imagem vertical padrão (1080x1920) com fundo escuro e título centralizado
    largura, altura = 1080, 1920
    cor_fundo = (15, 15, 25) # Tom escuro moderno
    
    imagem = Image.new("RGB", (largura, altura), color=cor_fundo)
    draw = ImageDraw.Draw(imagem)
    
    # Tenta carregar uma fonte padrão do Linux, senão usa a padrão do sistema
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()
        
    texto = titulo_episodio
    
    # Desenha o fundo visual básico para o Short (Corrigido para parênteses corretos)
    draw.rectangle([50, 800, 1030, 1120], fill=(30, 30, 45), outline=(100, 100, 200), width=4)
    draw.text((100, 930), texto, fill=(255, 255, 255), font=font)
    
    imagem.save(arquivo_saida)
    print(f"Imagem de fundo gerada: {arquivo_saida}")
    return arquivo_saida

if __name__ == "__main__":
    criar_imagem_fundo()
