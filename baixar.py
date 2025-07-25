import os
import requests

# Link da imagem no GitHub
IMAGEM_URL = "https://github.com/ReChat-game/Baixar/blob/main/BackgroundEraser_20250721_215310135.png"

# Caminho para salvar as imagens
CAMINHO_SALVAR = "/storage/emulated/0/Download/imagens_github"

# Criar pasta se não existir
os.makedirs(CAMINHO_SALVAR, exist_ok=True)

# Baixar 100 imagens
for i in range(1, 101):
    caminho_arquivo = os.path.join(CAMINHO_SALVAR, f"imagem_{i}.jpg")
    resposta = requests.get(IMAGEM_URL)

    if resposta.status_code == 200:
        with open(caminho_arquivo, "wb") as f:
            f.write(resposta.content)
        print(f"✅ Imagem {i} salva em {caminho_arquivo}")
    else:
        print(f"❌ Falha ao baixar imagem {i}: status {resposta.status_code}")

print("✅ Todas as imagens foram processadas.")
