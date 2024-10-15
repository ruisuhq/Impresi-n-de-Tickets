import win32print, tkinter as tk
from tkinter import ttk, messagebox

printer_name = "POS-80"

# Función para generar un ticket personalizado
def imprimir_ticket_personalizado():
    texto_ticket = entrada_texto.get("1.0", tk.END)
    if texto_ticket.strip():
        messagebox.showinfo("Imprimir Ticket", "Ticket personalizado enviado a la impresora")
        print_ticket(texto_ticket)
    else:
        messagebox.showwarning("Error", "El campo de ticket está vacío")

# Función para generar un ticket a partir de la plantilla predefinida
def generar_ticket_plantilla():
    producto1_cantidad = int(cantidad_producto1.get())
    producto2_cantidad = int(cantidad_producto2.get())
    producto3_cantidad = int(cantidad_producto3.get())

    total = (producto1_cantidad * 10) + (producto2_cantidad * 20) + (producto3_cantidad * 15)

    ticket = f"""
            Seminario de Ingeniería de Software I
            ----------------------------
            Lista de productos:

            Producto 1 (10$): {producto1_cantidad} unidades
            Producto 2 (20$): {producto2_cantidad} unidades
            Producto 3 (15$): {producto3_cantidad} unidades
            ----------------------------
            Total: {total}$
            
            Gracias por su no-compra!
            """

    messagebox.showinfo("Imprimir Ticket", "Ticket de plantilla enviado a la impresora")
    print_ticket(ticket)  # Llamada a tu función de impresión

# Función para imprimir
def print_ticket(text):
    hPrinter = win32print.OpenPrinter(printer_name)
    
    # Secuencia de bytes para cortar el papel
    cut_paper = b'\x1D\x56\x01'  # Comando ESC/POS para cortar papel
    
    try:
        # Iniciar el trabajo de impresión
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Ticket", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        
        # Escribir el texto del ticket
        win32print.WritePrinter(hPrinter, text.encode('utf-8'))
        
        # Añadir salto de línea adicional para evitar que el texto se corte
        win32print.WritePrinter(hPrinter, b'\n\n')
        
        # Comando de corte de papel
        win32print.WritePrinter(hPrinter, cut_paper)
        
        # Finalizar página e impresión
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    
    finally:
        win32print.ClosePrinter(hPrinter)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Programa de impresión de tickets")
ventana.geometry("600x700")
ventana.configure(bg="#404040") #Gris

# Título
titulo = tk.Label(ventana, text="Programa de impresión de tickets\nSeminario de Ingeniería de Software I", font=("Arial", 20, "bold"), fg="white", bg="#404040")
titulo.pack(pady=10)

# Crear un marco para el ticket personalizado
frame_personalizado = ttk.LabelFrame(ventana, text="Ticket Personalizado", padding=(20, 10))
frame_personalizado.configure(style="Custom.TLabelframe")
frame_personalizado.pack(padx=20, pady=10, fill="both", expand="yes")

entrada_texto = tk.Text(frame_personalizado, height=10, width=40, bg="white", fg="gray", insertbackground="white", font=("Arial", 12, "bold"))
entrada_texto.pack(pady=5)

# Botón para imprimir ticket personalizado
boton_imprimir_personalizado = tk.Button(frame_personalizado, text="Imprimir Ticket Personalizado", command=imprimir_ticket_personalizado,
                                         bg="darkgreen", fg="white", activebackground="green", activeforeground="white", font=("Arial", 12, "bold"))
boton_imprimir_personalizado.pack(pady=10)

# Crear un marco para la plantilla de ticket
frame_plantilla = ttk.LabelFrame(ventana, text="Plantilla de Ticket", padding=(20, 10))
frame_plantilla.configure(style="Custom.TLabelframe")
frame_plantilla.pack(padx=20, pady=10, fill="both", expand="yes")

productos_frame = tk.Frame(frame_plantilla, bg="#404040")
productos_frame.pack(pady=5)

# Producto 1
tk.Label(productos_frame, text="Producto 1 (10$):", fg="white", bg="#404040", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
cantidad_producto1 = tk.Spinbox(productos_frame, from_=0, to=10, width=5, bg="white", fg="black", font=("Arial", 12, "bold"))
cantidad_producto1.grid(row=0, column=1, padx=10, pady=5)

# Producto 2
tk.Label(productos_frame, text="Producto 2 (20$):", fg="white", bg="#404040", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
cantidad_producto2 = tk.Spinbox(productos_frame, from_=0, to=10, width=5, bg="white", fg="black", font=("Arial", 12, "bold"))
cantidad_producto2.grid(row=1, column=1, padx=10, pady=5)

# Producto 3
tk.Label(productos_frame, text="Producto 3 (15$):", fg="white", bg="#404040", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=5)
cantidad_producto3 = tk.Spinbox(productos_frame, from_=0, to=10, width=5, bg="white", fg="black", font=("Arial", 12, "bold"))
cantidad_producto3.grid(row=2, column=1, padx=10, pady=5)

# Botón para generar ticket de la plantilla
boton_generar_ticket = tk.Button(frame_plantilla, text="Generar Ticket de Plantilla", command=generar_ticket_plantilla,
                                 bg="darkgreen", fg="white", activebackground="green", activeforeground="white", font=("Arial", 12, "bold"))
boton_generar_ticket.pack(pady=20)

# Estilos personalizados para ttk
style = ttk.Style()
style.configure("Custom.TLabelframe", background="#404040", foreground="white", font=("Arial", 12, "bold"))

# Ejecutar la ventana
ventana.mainloop()
