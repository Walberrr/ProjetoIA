import os
import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)
CORS(app)

MAX_LEN = 150


# --- CARREGAR ARQUIVOS ---

print("Carregando modelo e arquivos...")
# Tenta carregar os arquivos, se não achar, avisa o erro no console
try:
    model = tf.keras.models.load_model('modelo_news_v2.h5')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('categorias.pickle', 'rb') as handle:
        categories = pickle.load(handle)
    print("✅ Sistema pronto e arquivos carregados!")
except Exception as e:
    print(f"❌ ERRO CRÍTICO: Não foi possível carregar os arquivos do modelo: {e}")
    print("Verifique se 'modelo_news_v2.h5', 'tokenizer.pickle' e 'categorias.pickle' estão na pasta.")

# --- ROTA DO SITE (Essa era a que faltava!) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- ROTA DA INTELIGÊNCIA ---
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        texto_usuario = data.get('text', '')

        if not texto_usuario:
            return jsonify({'error': 'Texto vazio'}), 400

        sequences = tokenizer.texts_to_sequences([texto_usuario])
        padded = pad_sequences(sequences, maxlen=MAX_LEN)

        prediction = model.predict(padded)
        label_index = np.argmax(prediction)
        confidence = float(np.max(prediction))
        category_name = categories[label_index]

        return jsonify({
            'category': category_name,
            'confidence': f"{confidence * 100:.2f}%"
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)