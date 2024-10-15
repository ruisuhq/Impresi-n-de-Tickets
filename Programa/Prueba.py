import win32print
import win32ui
from PIL import Image, ImageWin

printer_name = "POS-80"  # Nombre de la impresora
ticket_text = "Hola mundo\nSeminario de Ingenieria de Software\nDattebayo\nGracias por su compra!\nProducto 1: $10.00\nProducto 2: $20.00\nTotal: $30.00"

# Función para enviar el ticket a la impresora
def print_ticket(text):
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Ticket", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, text.encode('utf-8'))
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

# Ejecutar la impresión
print_ticket(ticket_text)
