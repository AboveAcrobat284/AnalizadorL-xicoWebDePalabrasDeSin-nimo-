import tkinter as tk
from tkinter import ttk
import re

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
            word = match.group()
            if word in synonyms_dict:
                results.append((word, synonyms_dict[word], "X", "", "", line_number, ""))
            elif word.isdigit():
                results.append((word, "", "", "", "X", line_number, ""))
            elif not word.isalnum():
                results.append((word, "", "", "X", "", line_number, ""))
            else:
                results.append((word, word, "", "", "", line_number, "X"))

    return results

def analyze_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    analysis_result = lexical_analyzer(input_text, synonyms_dict)

    # Limpiar la tabla
    for row in tree.get_children():
        tree.delete(row)

    # Insertar resultados en la tabla
    for word, synonym, synonym_mark, char_mark, digit_mark, line_number, not_found_mark in analysis_result:
        tree.insert("", "end", values=(word, synonym, synonym_mark, char_mark, digit_mark, line_number, not_found_mark))

# Crear la ventana principal
root = tk.Tk()
root.title("Analizador Léxico con Sinónimos")

# Crear widgets
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

text_label = tk.Label(frame, text="Ingrese el texto a analizar:")
text_label.pack(anchor="w")

text_entry = tk.Text(frame, height=10, width=50)
text_entry.pack()

analyze_button = tk.Button(frame, text="Analizar", command=analyze_text)
analyze_button.pack(pady=10)

# Crear el Treeview para mostrar los resultados
columns = ("Palabra ingresada", "Sinónimo de palabra", "Sinónimo", "Carácter", "Dígito", "Línea", "Palabra no encontrada")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("Palabra ingresada", text="Palabra ingresada")
tree.heading("Sinónimo de palabra", text="Sinónimo de palabra")
tree.heading("Sinónimo", text="Sinónimo")
tree.heading("Carácter", text="Carácter")
tree.heading("Dígito", text="Dígito")
tree.heading("Línea", text="Línea")
tree.heading("Palabra no encontrada", text="Palabra no encontrada")

tree.pack()

# Ajustar las columnas
for col in columns:
    tree.column(col, width=190, anchor="center")

# Iniciar el bucle principal de la aplicación
root.mainloop()
