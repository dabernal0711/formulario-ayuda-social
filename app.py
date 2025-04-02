from flask import Flask, render_template, request, send_file
from docx import Document
import uuid
import os

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    motivo = request.form['motivo']

    doc = Document('plantilla.docx')
    for p in doc.paragraphs:
        p.text = p.text.replace('{{nombre}}', nombre)
        p.text = p.text.replace('{{cedula}}', cedula)
        p.text = p.text.replace('{{motivo}}', motivo)

    filename = f'documento_{uuid.uuid4().hex}.docx'
    doc.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
