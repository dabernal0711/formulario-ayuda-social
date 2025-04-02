<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="2575.4">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; min-height: 14.0px}
  </style>
</head>
<body>
<p class="p1">from flask import Flask, render_template, request, send_file</p>
<p class="p1">from docx import Document</p>
<p class="p1">import uuid</p>
<p class="p1">import os</p>
<p class="p2"><br></p>
<p class="p1">app = Flask(__name__)</p>
<p class="p2"><br></p>
<p class="p1">@app.route('/')</p>
<p class="p1">def formulario():</p>
<p class="p1"><span class="Apple-converted-space">    </span>return render_template('formulario.html')</p>
<p class="p2"><br></p>
<p class="p1">@app.route('/enviar', methods=['POST'])</p>
<p class="p1">def enviar():</p>
<p class="p1"><span class="Apple-converted-space">    </span>nombre = request.form['nombre']</p>
<p class="p1"><span class="Apple-converted-space">    </span>cedula = request.form['cedula']</p>
<p class="p1"><span class="Apple-converted-space">    </span>motivo = request.form['motivo']</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>doc = Document('plantilla.docx')</p>
<p class="p1"><span class="Apple-converted-space">    </span>for p in doc.paragraphs:</p>
<p class="p1"><span class="Apple-converted-space">        </span>p.text = p.text.replace('{{nombre}}', nombre)</p>
<p class="p1"><span class="Apple-converted-space">        </span>p.text = p.text.replace('{{cedula}}', cedula)</p>
<p class="p1"><span class="Apple-converted-space">        </span>p.text = p.text.replace('{{motivo}}', motivo)</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>filename = f'documento_{uuid.uuid4().hex}.docx'</p>
<p class="p1"><span class="Apple-converted-space">    </span>doc.save(filename)</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>return send_file(filename, as_attachment=True)</p>
<p class="p2"><br></p>
<p class="p1">if __name__ == '__main__':</p>
<p class="p1"><span class="Apple-converted-space">    </span>app.run()</p>
</body>
</html>
