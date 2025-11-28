import os
import shutil

print("--- INICIANDO CORREÇÃO DE PASTAS ---")

# 1. Garante que a pasta templates existe
if not os.path.exists('templates'):
    os.makedirs('templates')
    print("✅ Pasta 'templates' foi criada.")
else:
    print("ℹ️ A pasta 'templates' já existe.")

# 2. Procura o index.html e move para lá
if os.path.exists('index.html'):
    shutil.move('index.html', 'templates/index.html')
    print("✅ SUCESSO: Arquivo 'index.html' movido para dentro de 'templates'.")
elif os.path.exists('templates/index.html'):
    print("✅ O arquivo 'index.html' já está no lugar certo.")
else:
    print("❌ ERRO CRÍTICO: Não encontrei o arquivo 'index.html' nem na raiz, nem na pasta templates.")
    print("Você precisa criar o arquivo index.html novamente.")

print("-" * 30)
print("VERIFICAÇÃO FINAL:")
if os.path.exists('templates/index.html'):
    print("Tudo pronto! Pode rodar o app.py.")
else:
    print("Ainda falta o arquivo index.html.")