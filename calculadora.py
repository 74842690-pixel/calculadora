
import tkinter as tk
from tkinter import ttk, messagebox
import re


class Formulario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario de Registro - Semana 13")
        self.ventana.geometry("520x680")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#eef2f7")

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="REGISTRO DE USUARIO",
            font=("Arial", 19, "bold"),
            bg="#eef2f7",
            fg="#17365d"
        )
        titulo.pack(pady=15)

        subtitulo = tk.Label(
            self.ventana,
            text="Complete todos los campos del formulario",
            font=("Arial", 10),
            bg="#eef2f7",
            fg="#555555"
        )
        subtitulo.pack(pady=2)

        panel = tk.Frame(
            self.ventana,
            bg="white",
            padx=30,
            pady=15
        )
        panel.pack(padx=25, pady=15, fill="both", expand=True)

        # Nombre
        self.crear_etiqueta(panel, "Nombre completo:")
        self.nombre = ttk.Entry(panel, font=("Arial", 11))
        self.nombre.pack(fill="x", pady=4)

        # Correo electrónico
        self.crear_etiqueta(panel, "Correo electrónico:")
        self.email = ttk.Entry(panel, font=("Arial", 11))
        self.email.pack(fill="x", pady=4)

        # Contraseña
        self.crear_etiqueta(panel, "Contraseña:")
        self.password = ttk.Entry(
            panel,
            font=("Arial", 11),
            show="*"
        )
        self.password.pack(fill="x", pady=4)

        # Confirmación
        self.crear_etiqueta(panel, "Confirmar contraseña:")
        self.confirmar = ttk.Entry(
            panel,
            font=("Arial", 11),
            show="*"
        )
        self.confirmar.pack(fill="x", pady=4)

        # Edad
        self.crear_etiqueta(panel, "Edad:")
        self.edad = ttk.Entry(panel, font=("Arial", 11))
        self.edad.pack(fill="x", pady=4)

        # Género
        self.crear_etiqueta(panel, "Género:")
        self.genero = ttk.Combobox(
            panel,
            values=["Masculino", "Femenino", "Otro"],
            state="readonly",
            font=("Arial", 11)
        )
        self.genero.set("Seleccionar género")
        self.genero.pack(fill="x", pady=4)

        # Términos y condiciones
        self.acepta = tk.BooleanVar(value=False)

        tk.Checkbutton(
            panel,
            text="Acepto los términos y condiciones",
            variable=self.acepta,
            bg="white",
            font=("Arial", 10),
            activebackground="white"
        ).pack(anchor="w", pady=12)

        # Botones
        botones = tk.Frame(panel, bg="white")
        botones.pack(pady=12)

        tk.Button(
            botones,
            text="REGISTRAR",
            command=self.registrar,
            bg="#1769aa",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            cursor="hand2"
        ).pack(side="left", padx=6)

        tk.Button(
            botones,
            text="LIMPIAR",
            command=self.limpiar,
            bg="#d9534f",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            cursor="hand2"
        ).pack(side="left", padx=6)

        self.nombre.focus()

    def crear_etiqueta(self, panel, texto):
        tk.Label(
            panel,
            text=texto,
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#333333"
        ).pack(anchor="w", pady=(6, 0))

    def validar_datos(self):
        nombre = self.nombre.get().strip()
        email = self.email.get().strip()
        password = self.password.get()
        confirmar = self.confirmar.get()
        edad = self.edad.get().strip()
        genero = self.genero.get()

        if not nombre:
            messagebox.showwarning(
                "Validación",
                "Ingresa tu nombre completo."
            )
            self.nombre.focus()
            return False

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]+", nombre):
            messagebox.showwarning(
                "Validación",
                "El nombre contiene caracteres no permitidos."
            )
            self.nombre.focus()
            return False

        patron_email = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"

        if not re.fullmatch(patron_email, email):
            messagebox.showwarning(
                "Validación",
                "Ingresa un correo electrónico válido."
            )
            self.email.focus()
            return False

        if len(password) < 8:
            messagebox.showwarning(
                "Validación",
                "La contraseña debe tener al menos 8 caracteres."
            )
            self.password.focus()
            return False

        if not re.search(r"[A-Z]", password):
            messagebox.showwarning(
                "Validación",
                "La contraseña debe contener una letra mayúscula."
            )
            self.password.focus()
            return False

        if not re.search(r"[a-z]", password):
            messagebox.showwarning(
                "Validación",
                "La contraseña debe contener una letra minúscula."
            )
            self.password.focus()
            return False

        if not re.search(r"\d", password):
            messagebox.showwarning(
                "Validación",
                "La contraseña debe contener un número."
            )
            self.password.focus()
            return False

        if password != confirmar:
            messagebox.showwarning(
                "Validación",
                "Las contraseñas no coinciden."
            )
            self.confirmar.focus()
            return False

        try:
            edad_numero = int(edad)

            if edad_numero < 15:
                messagebox.showwarning(
                    "Validación",
                    "La edad mínima permitida es 15 años."
                )
                self.edad.focus()
                return False

            if edad_numero > 120:
                messagebox.showwarning(
                    "Validación",
                    "Ingresa una edad válida."
                )
                self.edad.focus()
                return False

        except ValueError:
            messagebox.showwarning(
                "Validación",
                "La edad debe ser un número entero."
            )
            self.edad.focus()
            return False

        if genero not in ["Masculino", "Femenino", "Otro"]:
            messagebox.showwarning(
                "Validación",
                "Selecciona un género."
            )
            self.genero.focus()
            return False

        if not self.acepta.get():
            messagebox.showwarning(
                "Validación",
                "Debes aceptar los términos y condiciones."
            )
            return False

        return True

    def registrar(self):
        if self.validar_datos():
            messagebox.showinfo(
                "Registro exitoso",
                "¡El usuario se registró correctamente!"
            )
            self.limpiar()

    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.confirmar.delete(0, tk.END)
        self.edad.delete(0, tk.END)
        self.genero.set("Seleccionar género")
        self.acepta.set(False)
        self.nombre.focus()


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Formulario(ventana)
    ventana.mainloop()
