# apar ejecutar Abre tu navegador.Escribe localhost:5000 en la barra de direcciones.

from flask import Flask, render_template

app = Flask(__name__)

# Lista de productos con imágenes que cargan rápido
productos = [
    {"nombre": "Cafe de Grano", "precio": 5000, "imagen": "cafe.webp"},
    {"nombre": "Te Organico", "precio": 3500, "imagen": "teorganico.webp"},
    {"nombre": "Muffin Arandano", "precio": 1500, "imagen": "muffi.webp"}
]

@app.route('/')
def home():
    return render_template('index.html', lista=productos)

if __name__ == '__main__':
    app.run(debug=True)