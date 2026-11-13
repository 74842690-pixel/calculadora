
import tkinter as tk
from tkinter import ttk, messagebox


class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora - Semana 13")
        self.ventana.geometry("430x430")
        self.ventana.resizable(False, False)

        self.ventana.configure(bg="#eef2f7")

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="CALCULADORA",
            font=("Arial", 20, "bold"),
            bg="#eef2f7",
            fg="#17365d"
        )
        titulo.pack(pady=20)

        panel = tk.Frame(self.ventana, bg="white", padx=25, pady=20)
        panel.pack(padx=20, fill="both", expand=True)

        tk.Label(
            panel, text="Primer número:",
            font=("Arial", 11), bg="white"
        ).pack(anchor="w", pady=5)

        self.numero1 = ttk.Entry(panel, font=("Arial", 12))
        self.numero1.pack(fill="x", pady=5)

        tk.Label(
            panel, text="Segundo número:",
            font=("Arial", 11), bg="white"
        ).pack(anchor="w", pady=5)

        self.numero2 = ttk.Entry(panel, font=("Arial", 12))
        self.numero2.pack(fill="x", pady=5)

        tk.Label(
            panel, text="Selecciona una operación:",
            font=("Arial", 11), bg="white"
        ).pack(anchor="w", pady=8)

        self.operacion = ttk.Combobox(
            panel,
            values=["Sumar (+)", "Restar (-)",
                    "Multiplicar (*)", "Dividir (/)"],
            state="readonly",
            font=("Arial", 11)
        )
        self.operacion.current(0)
        self.operacion.pack(fill="x", pady=5)

        botones = tk.Frame(panel, bg="white")
        botones.pack(pady=15)

        tk.Button(
            botones,
            text="CALCULAR",
            command=self.calcular,
            bg="#1769aa",
            fg="white",
            font=("Arial", 10, "bold"),
            width=13,
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Button(
            botones,
            text="LIMPIAR (C)",
            command=self.limpiar,
            bg="#d9534f",
            fg="white",
            font=("Arial", 10, "bold"),
            width=13,
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Label(
            panel,
            text="Resultado:",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(pady=5)

        self.resultado = tk.Label(
            panel,
            text="Esperando operación...",
            font=("Arial", 16, "bold"),
            bg="#e8f1fc",
            fg="#17365d",
            width=25,
            pady=12
        )
        self.resultado.pack(fill="x", pady=5)

        self.ventana.bind("<Return>", lambda event: self.calcular())

    def calcular(self):
        try:
            n1 = float(self.numero1.get())
            n2 = float(self.numero2.get())

            operacion = self.operacion.get()

            if operacion == "Sumar (+)":
                respuesta = n1 + n2

            elif operacion == "Restar (-)":
                respuesta = n1 - n2

            elif operacion == "Multiplicar (*)":
                respuesta = n1 * n2

            elif operacion == "Dividir (/)":
                if n2 == 0:
                    raise ZeroDivisionError
                respuesta = n1 / n2

            else:
                messagebox.showwarning(
                    "Advertencia",
                    "Selecciona una operación."
                )
                return

            self.resultado.config(
                text=f"{respuesta:g}",
                fg="#16803c"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingresa números válidos en ambos campos."
            )
            self.resultado.config(text="Error en los datos", fg="red")

        except ZeroDivisionError:
            messagebox.showerror(
                "Error",
                "No se puede dividir entre cero."
            )
            self.resultado.config(text="División no permitida", fg="red")

    def limpiar(self):
        self.numero1.delete(0, tk.END)
        self.numero2.delete(0, tk.END)
        self.operacion.current(0)
        self.resultado.config(
            text="Esperando operación...",
            fg="#17365d"
        )
        self.numero1.focus()


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Calculadora(ventana)
    ventana.mainloop()
