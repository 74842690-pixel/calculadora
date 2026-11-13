import tkinter as tk
from tkinter import messagebox
import re


class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora - Semana 13")
        self.ventana.geometry("320x410")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#eeeeee")

        self.display = tk.Entry(
            self.ventana,
            font=("Arial", 24),
            justify="right",
            bd=5,
            relief="sunken"
        )
        self.display.grid(
            row=0, column=0, columnspan=4,
            sticky="nsew", padx=8, pady=10, ipady=8
        )
        self.display.focus_set()

        botones = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("C", "0", "=", "+")
        ]

        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                color = "#d9e8f5" if texto in "+-*/" else "#ffffff"
                if texto == "C":
                    color = "#ffd6d6"
                elif texto == "=":
                    color = "#bde5c8"

                boton = tk.Button(
                    self.ventana,
                    text=texto,
                    font=("Arial", 18, "bold"),
                    width=5,
                    height=2,
                    bg=color,
                    command=lambda valor=texto: self.click(valor)
                )
                boton.grid(row=i + 1, column=j, padx=4, pady=4, sticky="nsew")

        for columna in range(4):
            self.ventana.grid_columnconfigure(columna, weight=1)

        self.ventana.bind("<Return>", lambda evento: self.click("="))
        self.ventana.bind("<Escape>", lambda evento: self.click("C"))

    def click(self, valor):
        if valor == "C":
            self.display.delete(0, tk.END)
        elif valor == "=":
            expresion = self.display.get().strip()
            # Solo permite números, punto decimal y operadores básicos.
            if not expresion or not re.fullmatch(r"[0-9+*/(). -]+", expresion):
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)
                return
            try:
                resultado = eval(expresion, {"__builtins__": {}}, {})
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except (SyntaxError, ZeroDivisionError, TypeError, NameError):
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, valor)

    def run(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    Calculadora().run()
