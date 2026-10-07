import os
import requests
from PIL import Image
from urllib.parse import quote

def criar_imagem_fundo(categoria="terror", texto_roteiro="historia misteriosa", arquivo_saida="output_bg.png"):
    print(f"A gerar imagem por IA para o tema '{categoria}'...")
    
    # Define estilos visuais profissionais com base na categoria
    estilos = {
        "terror": "dark horror cinematic style, spooky atmosphere, high contrast, highly detailed digital art",
        "medieval": "epic medieval fantasy painting, ancient castle, dramatic lighting, detailed digital artwork",
        "misterio": "dark mystery, foggy night, cinematic shadows, thriller atmosphere",
        "motivacional": "majestic cinematic landscape, epic sunset, inspiring horizon, 8k resolution"
    }
    
    estilo_escolhido = estilos.get(categoria, "cinematic dark fantasy")
    resumo = texto_roteiro[:120].replace("\n", " ")
    prompt_final = f"{resumo}, {estilo_escolhido}, vertical format 9:16"
    
    prompt_url = quote(prompt_final)
    url_ia = f"https://image.pollinations.ai/prompt/{prompt_url}?width=1080&height=1920&nologo=true&seed=123"
    
    sucesso = False
    try:
        response = requests.get(url_ia, timeout=40)
        if response.status_code == 200 and len(response.content) > 3000:
            with open(arquivo_saida, 'wb') as f:
                f.write(response.content)
            
            # Aplica uma camada escura por cima para o texto do Short sobressair perfeitamente
            img = Image.open(arquivo_saida).convert("RGBA")
            overlay = Image.new("RGBA", img.size, (0, 0, 0, 140))
            img_combinada = Image.alpha_composite(img, overlay).convert("RGB")
            img_combinada.save(arquivo_saida)
            sucesso = True
            print("Imagem exclusiva gerada com sucesso e aplicada ao vídeo!")
    except Exception as e:
        print(f"Erro ao obter imagem da IA: {e}")

    if not sucesso:
        print("A utilizar fundo alternativo de segurança...")
        largura, altura = 1080, 1920
        imagem = Image.new("RGB", (largura, altura), color=(15, 15, 25))
        imagem.save(arquivo_saida)
        
    return arquivo_saida

if __name__ == "__main__":
    criar_imagem_fundo("terror", "um segredo escondido na floresta")
