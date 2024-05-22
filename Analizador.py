from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# Diccionario de sinónimos
synonyms_dict = {
    "rápido": "veloz",
    "lento": "pausado",
    "inteligente": "listo",
    "feliz": "contento",
    "triste": "afligido",
    "grande": "enorme",
    "pequeño": "diminuto",
    "fuerte": "robusto",
    "débil": "frágil",
    "bonito": "hermoso",
    "feo": "horrible",
    "amable": "cortés",
    "grosero": "rudo",
    "amigo": "compañero",
    "enemigo": "adversario",
    "trabajo": "empleo",
    "dinero": "plata",
    "casa": "hogar",
    "coche": "automóvil",
    "bicicleta": "bici",
    "mujer": "dama",
    "hombre": "caballero",
    "niño": "chico",
    "niña": "chica",
    "perro": "can",
    "gato": "felino",
    "cielo": "firmamento",
    "tierra": "suelo",
    "mar": "océano",
    "lago": "laguna",
    "rio": "arroyo",
    "montaña": "cerro",
    "valle": "depresión",
    "bosque": "selva",
    "desierto": "arenal",
    "ciudad": "metrópolis",
    "pueblo": "aldea",
    "camino": "sendero",
    "carretera": "autopista",
    "edificio": "estructura",
    "puente": "viaducto",
    "ciencia": "sabiduría",
    "arte": "creación",
    "música": "melodía",
    "libro": "volumen",
    "película": "filme",
    "juego": "diversión",
    "computadora": "ordenador",
    "teléfono": "móvil",
    "reloj": "cronómetro"
}

def lexical_analyzer(text, synonyms_dict):
    pattern = re.compile(r'\b\w+\b|\d+|[^\w\s]')
    results = []
    lines = text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        for match in pattern.finditer(line):
            word = match.group().lower()  # Convertir la palabra a minúsculas para comparar
            if word in synonyms_dict:
                synonym = synonyms_dict[word]  # Obtener el sinónimo
                results.append((word, synonym, "X", "", "", line_number, ""))
            elif word.isdigit():
                results.append((word, "", "", "", "X", line_number, ""))
            elif not word.isalnum():
                results.append((word, "", "", "X", "", line_number, ""))
            else:
                results.append((word, word, "", "", "", line_number, "X"))

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_result = []
    if request.method == 'POST':
        input_text = request.form['input_text']
        analysis_result = lexical_analyzer(input_text, synonyms_dict)

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Analizador Léxico con Sinónimos</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    width: 60%;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                form {
                    text-align: center;
                }
                textarea {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }
                th {
                    background-color: #f2f2f2;
                }
                .center {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Analizador Léxico con Sinónimos</h1>
                <form method="POST">
                    <textarea name="input_text" rows="10" placeholder="Ingrese el texto a analizar...">{{ request.form['input_text'] if request.method == 'POST' else '' }}</textarea><br>
                    <input type="submit" value="Analizar">
                </form>
                {% if analysis_result %}
                <table>
                    <tr>
                        <th>Palabra ingresada</th>
                        <th>Sinónimo de palabra</th>
                        <th class="center">Sinónimo</th>
                        <th class="center">Carácter</th>
                        <th class="center">Dígito</th>
                        <th class="center">Línea</th>
                        <th class="center">Palabra no encontrada</th>
                    </tr>
                    {% for result in analysis_result %}
                    <tr>
                        <td>{{ result[0] }}</td>
                        <td>{{ result[1] }}</td>
                        <td class="center">{{ result[2] }}</td>
                        <td class="center">{{ result[3] }}</td>
                        <td class="center">{{ result[4] }}</td>
                        <td class="center">{{ result[5] }}</td>
                        <td class="center">{{ result[6] }}</td>
                    </tr>
                    {% endfor %}
                </table>
                {% endif %}
            </div>
        </body>
        </html>
    ''', analysis_result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
