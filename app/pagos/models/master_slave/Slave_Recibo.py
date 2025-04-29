# Slave_Recibo.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import os

class Slave_Recibo:
    def generar_recibo(self, numero_transaccion, paciente, concepto, monto, metodo_pago):
        """
        Genera y guarda un recibo en formato PDF con los datos proporcionados.
        El archivo se guarda en la carpeta media/recibos/
        """
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Definir la ruta donde se guardará el recibo
        ruta_directorio = "media/recibos"
        os.makedirs(ruta_directorio, exist_ok=True)  # Crea la carpeta si no existe
        
        nombre_archivo = os.path.join(ruta_directorio, f"recibo_{numero_transaccion}.pdf")
        
        # Crear el PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        textobject = c.beginText(50, 750)
        textobject.setFont("Helvetica-Bold", 16)
        textobject.textLine("Recibo de Pago")
        textobject.setFont("Helvetica", 12)
        textobject.textLine(f"Número de Transacción: {numero_transaccion}")
        textobject.textLine(f"Fecha: {fecha_actual}")
        textobject.textLine(f"Paciente: {paciente}")
        textobject.textLine(f"Concepto: {concepto}")
        textobject.textLine(f"Monto: ${float(monto):.2f}")
        textobject.textLine(f"Método de Pago: {metodo_pago}")
        c.drawText(textobject)
        c.save()
        
        return nombre_archivo
