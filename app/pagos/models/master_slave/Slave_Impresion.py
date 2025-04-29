# Slave_Impresion.py
import os
import platform

class Slave_Impresion:
    def imprimir_recibo(self, ruta_archivo_pdf):
        """
        Permite imprimir el recibo en una impresora.
        """
        print(f"Simulando la impresión del recibo: {ruta_archivo_pdf}")
        sistema_operativo = platform.system()
        if sistema_operativo == "Windows":
            try:
                os.startfile(ruta_archivo_pdf, "print")
                print("Comando de impresión enviado (Windows).")
            except Exception as e:
                print(f"Error al intentar imprimir en Windows: {e}")
        elif sistema_operativo == "Linux":
            try:
                os.system(f"lp {ruta_archivo_pdf}")
                print("Comando de impresión enviado (Linux).")
            except Exception as e:
                print(f"Error al intentar imprimir en Linux: {e}")
        elif sistema_operativo == "Darwin":  # macOS
            try:
                os.system(f"lpr {ruta_archivo_pdf}")
                print("Comando de impresión enviado (macOS).")
            except Exception as e:
                print(f"Error al intentar imprimir en macOS: {e}")
        else:
            print(f"Impresión no soportada en el sistema operativo: {sistema_operativo}")