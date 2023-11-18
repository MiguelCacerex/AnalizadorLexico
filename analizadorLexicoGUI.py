import tkinter as tk
from tkinter import ttk


class AnalizadorLexicoGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Analizador Lexico - Teoria lenguajes formales")
        self.ancho_ventana = 450
        self.alto_ventana = 500
        self.posicion_x = 100
        self.posicion_y = 50

        dimensiones_ventana = "{}x{}+{}+{}".format(
            self.ancho_ventana, self.alto_ventana, self.posicion_x, self.posicion_y)
        self.ventana.geometry(dimensiones_ventana)

        # Crear el área de texto
        self.entrada_texto = tk.Text(self.ventana, height=10, width=40)
        self.entrada_texto.pack(pady=10)

        # Crear el botón
        self.boton_agregar = tk.Button(
            self.ventana, text="Generar Analisis Lexico", command=self.agregar_a_tabla)
        self.boton_agregar.pack(pady=10)

        # Crear la tabla con tres columnas
        self.columnas = ('Lexema', 'Categoria', 'Posicion')
        self.tabla = ttk.Treeview(
            self.ventana, columns=self.columnas, show='headings')

        # Configurar las columnas
        for col in self.columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)

        self.tabla.pack(pady=20)

    def agregar_a_tabla(self):
        texto = self.entrada_texto.get("1.0", tk.END).strip()
        if texto:
            self.tabla.insert('', 'end', values=(
                texto, texto.upper(), texto.lower()))
            self.entrada_texto.delete("1.0", tk.END)

    def iniciar(self):
        # Iniciar el bucle de eventos
        self.ventana.mainloop()
