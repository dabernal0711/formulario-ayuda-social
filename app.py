from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

DB_PATH = 'formulario.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            solicitante_nombre TEXT,
            solicitante_cedula TEXT,
            fecha TEXT,
            datos_json TEXT
        )''')
        conn.commit()

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('solicitante_nombre')
    cedula = request.form.get('solicitante_cedula')
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datos_completos = dict(request.form)

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT fecha FROM solicitudes WHERE solicitante_cedula = ?", (cedula,))
        resultado = c.fetchone()

        if resultado:
            mensaje = f"La cédula {cedula} ya fue registrada anteriormente el {resultado[0]}."
            flash(mensaje, "warning")
            return redirect(url_for('formulario'))

        # Insertar nueva solicitud
        c.execute("INSERT INTO solicitudes (solicitante_nombre, solicitante_cedula, fecha, datos_json) VALUES (?, ?, ?, ?)",
                  (nombre, cedula, fecha, str(datos_completos)))
        conn.commit()

    flash("Solicitud registrada exitosamente", "success")
    return redirect(url_for('formulario'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
