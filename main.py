# main.py
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Отправляем файл index.html из текущей папки
    return send_from_directory('.', 'index.html2')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)