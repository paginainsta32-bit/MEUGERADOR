import os
import random
import requests
from PIL import Image, ImageDraw, ImageFont

def criar_imagem_fundo(categoria="terror", titulo_episodio="Episódio 01", arquivo_saida="output_bg.png"):
    print(f"A obter imagem de fundo fiável para o tema: {categoria}...")
    
    # Bancos de imagens verticais garantidos e gratuitos por categoria (Picsum com IDs específicos temáticos/escuros)
    imagens_por_categoria = {
        "terror": [
            "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=1080&q=80", # Floresta escura
            "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1080&q=80"  # Noite sombria
        ],
        "medieval": [
            "https://images.unsplash.com/photo-1599839575943-a7e366bc503a?auto=format&fit=crop&w=1080&q=80", # Castelo / Épico
            "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1080&q=80"  # Atmosfera antiga
        ],
        "misterio": [
            "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?auto=format&fit=crop&w=1080&q=80", # Nevoeiro / Sombra
            "https://images.unsplash.com/photo-1514539079130-25950c84af65?auto=format&fit=crop&w=1080&q=80"  # Noite misteriosa
        ],
        "motivacional": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1080&q=80", # Paisagem / Horizonte
            "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1080&q=80"  # Natureza ampla
        ]
    }
    
    # Seleciona uma lista de links com base na categoria ou usa uma predefinição
    lista_links = imagens_por_categoria.get(categoria, imagens_por_categoria["terror"])
    url_escolhida = random.choice(lista_links)
    
    sucesso = False
    try:
        response = requests.get(url_escolhida, timeout=15)
        if response.status_code == 200:
            with open(arquivo_saida, 'wb') as f:
                f.write(response.content)
            
            # Aplica uma camada escura semi-transparente por cima para destacar o texto
            img = Image.open(arquivo_saida).convert("RGBA")
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 140)) # Camada de contraste
            img_combinada = Image.alpha_composite(img, overlay).convert("RGB")
            img_combinada.save(arquivo_saida)
            sucesso = True
            print(f"Imagem de fundo aplicada com sucesso!")
    except Exception as e:
        print(f"Erro ao descarregar imagem: {e}")
        
    if not sucesso:
        # Fundo texturizado alternativo de segurança caso haja falha de rede
        largura, altura = 1080, 1920
        imagem = Image.new("RGB", (largura, altura), color=(25, 25, 35))
        imagem.save(arquivo_saida)
        
    return arquivo_saida

if __name__ == "__main__":
    criar_imagem_fundo("terror", "Teste")
