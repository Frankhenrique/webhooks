from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook_rcs', methods=['POST'])
def webhook_rcs():
    dados = request.get_json()
    print("🔄 Redirecionando para o servidor interno...")
    try:
        r = requests.post("http://177.26.126.215:5000/webhook_rcs", json=dados, timeout=3)
        print("✅ Encaminhado:", r.status_code)
    except Exception as e:
        print("❌ Erro ao enviar:", str(e))
    return jsonify(status="ok")
