import os
import requests
from PIL import Image, ImageDraw, ImageFont

def criar_imagem_fundo(categoria="terror", titulo_episodio="Episódio 01", arquivo_saida="output_bg.png"):
    print(f"A gerar imagens contextuais para o tema: {categoria}...")
    
    # Mapeia palavras-chave visuais baseadas na categoria escolhida no painel
    termos_visuais = {
        "terror": "dark forest, spooky, mysterious, night, horror",
        "medieval": "medieval castle, knight, epic, vintage, old stones",
        "misterio": "fog, detective, dark room, secret, shadow",
        "motivacional": "sunset, mountains, success, inspiration, horizon"
    }
    
    # Seleciona o termo de busca ou usa um padrão genérico escuro
    termo = termos_visuais.get(categoria, "dark cinematic background")
    
    # URL de imagens dinâmicas baseadas em termos (usando Unsplash Source de forma gratuita)
    url = f"https://source.unsplash.com/1080x1920/?{termo.replace(' ', ',')}"
    
    try:
        # Tenta obter uma imagem contextualizada da web
        response = requests.get(url, timeout=15)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(arquivo_saida, 'wb') as f:
                f.write(response.content)
            
            # Aplica uma camada escura semi-transparente para destacar o texto sobre a imagem
            img = Image.open(arquivo_saida).convert("RGBA")
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 150)) # Escurece para legibilidade
            img_combinada = Image.alpha_composite(img, overlay).convert("RGB")
            img_combinada.save(arquivo_saida)
            
            print(f"Imagem temática aplicada com sucesso para '{categoria}': {arquivo_saida}")
            return arquivo_saida
    except Exception as e:
        print(f"Aviso ao buscar imagem temática: {e}. A usar fundo de segurança.")
        
    # Fallback visual caso a rede falhe: cria um fundo escuro elegante
    largura, altura = 1080, 1920
    imagem = Image.new("RGB", (largura, altura), color=(15, 15, 25))
    draw = ImageDraw.Draw(imagem)
    draw.rectangle([50, 800, 1030, 1120], fill=(30, 30, 45), outline=(100, 100, 200), width=4)
    imagem.save(arquivo_saida)
    return arquivo_saida

if __name__ == "__main__":
    criar_imagem_fundo("terror", "Teste de Categoria")
