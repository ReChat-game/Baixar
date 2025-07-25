import os
import requests
from concurrent.futures import ThreadPoolExecutor

IMAGEM_URL = "https://raw.githubusercontent.com/ReChat-game/Baixar/main/BackgroundEraser_20250721_215310135.png"
CAMINHO_SALVAR = "/storage/emulated/0/Download/imagens_github"

os.makedirs(CAMINHO_SALVAR, exist_ok=True)

def baixar_imagem(i):
    caminho_arquivo = os.path.join(CAMINHO_SALVAR, f"imagem_{i}.png")
    try:
        resposta = requests.get(IMAGEM_URL)
        if resposta.status_code == 200:
            with open(caminho_arquivo, "wb") as f:
                f.write(resposta.content)
            print(f"✅ Imagem {i} salva como imagem_{i}.png")
        else:
            print(f"❌ Falha na imagem {i}: HTTP {resposta.status_code}")
    except Exception as e:
        print(f"❌ Erro na imagem {i}: {e}")

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(baixar_imagem, range(1, 101))

print("🎉 Todas as 100 imagens foram baixadas em paralelo.")
