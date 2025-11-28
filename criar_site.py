import os

html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Classificador de Notícias IA</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #e9ecef; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 2.5rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 100%; max-width: 500px; }
        h2 { text-align: center; color: #495057; margin-bottom: 20px; }
        p { color: #6c757d; font-size: 0.9rem; margin-bottom: 5px; }
        textarea { width: 100%; height: 120px; padding: 15px; margin-bottom: 15px; border: 1px solid #ced4da; border-radius: 8px; font-size: 1rem; resize: none; box-sizing: border-box; }
        textarea:focus { outline: none; border-color: #80bdff; box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25); }
        button { width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: 600; transition: background 0.2s; }
        button:hover { background-color: #0056b3; }
        #result { margin-top: 25px; text-align: center; padding: 15px; border-radius: 8px; display: none; }
        .success { background-color: #d1e7dd; color: #0f5132; border: 1px solid #badbcc; }
        .error { background-color: #f8d7da; color: #842029; border: 1px solid #f5c2c7; }
    </style>
</head>
<body>
<div class="container">
    <h2>🤖 IA de Notícias</h2>
    <p>Cole a manchete (em inglês):</p>
    <textarea id="newsText" placeholder="Ex: NASA discovers new planet with water..."></textarea>
    <button onclick="classifyNews()" id="btnClassify">Classificar Notícia</button>
    <div id="result"></div>
</div>
<script>
    async function classifyNews() {
        const text = document.getElementById('newsText').value;
        const resultDiv = document.getElementById('result');
        const btn = document.getElementById('btnClassify');
        
        if(!text.trim()) return;

        resultDiv.style.display = 'block';
        resultDiv.className = ''; 
        resultDiv.style.backgroundColor = '#e2e3e5';
        resultDiv.innerText = 'Processando...';
        btn.disabled = true;

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            const data = await response.json();
            
            if (data.error) {
                resultDiv.innerText = 'Erro: ' + data.error;
                resultDiv.className = 'error';
            } else {
                resultDiv.innerHTML = `<strong>Categoria:</strong> ${data.category}<br><strong>Confiança:</strong> ${data.confidence}`;
                resultDiv.className = 'success';
            }
        } catch (error) {
            resultDiv.innerText = 'Erro de conexão com o servidor.';
            resultDiv.className = 'error';
        }
        btn.disabled = false;
    }
</script>
</body>
</html>
"""

# 1. Garante que a pasta existe
print("🔧 Verificando pasta 'templates'...")
if not os.path.exists('templates'):
    os.makedirs('templates')
    print("✅ Pasta 'templates' CRIADA.")
else:
    print("ℹ️ Pasta 'templates' já existia.")

# 2. Escreve o arquivo index.html LÁ DENTRO
caminho_arquivo = os.path.join('templates', 'index.html')

with open(caminho_arquivo, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ ARQUIVO SALVO COM SUCESSO EM: {os.path.abspath(caminho_arquivo)}")
print("Pode rodar o app.py agora!")