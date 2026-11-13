import tkinter as tk
from tkinter import messagebox
import re


class FormularioRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Usuario - Semana 13")
        self.root.geometry("540x590")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f8")

        self.nombre = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_pass = tk.StringVar()
        self.edad = tk.StringVar()
        self.genero = tk.StringVar(value="")
        self.acepto = tk.BooleanVar(value=False)

        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root, padx=25, pady=20, bg="#f4f6f8")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame, text="Registro de Usuario",
            font=("Arial", 19, "bold"), bg="#f4f6f8", fg="#203040"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        campos = [
            ("Nombre completo:", self.nombre, False),
            ("Email:", self.email, False),
            ("Contraseña:", self.password, True),
            ("Confirmar contraseña:", self.confirm_pass, True),
            ("Edad:", self.edad, False),
        ]

        self.entradas = []
        for i, (etiqueta, variable, oculto) in enumerate(campos, start=1):
            tk.Label(
                frame, text=etiqueta, font=("Arial", 11),
                bg="#f4f6f8"
            ).grid(row=i, column=0, sticky="e", pady=8, padx=(0, 12))

            entrada = tk.Entry(
                frame, textvariable=variable, width=32,
                font=("Arial", 11), show="*" if oculto else ""
            )
            entrada.grid(row=i, column=1, sticky="w", pady=8, ipady=4)
            self.entradas.append(entrada)

        tk.Label(
            frame, text="Género:", font=("Arial", 11), bg="#f4f6f8"
        ).grid(row=6, column=0, sticky="e", pady=8, padx=(0, 12))

        genero_frame = tk.Frame(frame, bg="#f4f6f8")
        genero_frame.grid(row=6, column=1, sticky="w")
        for opcion in ("Masculino", "Femenino", "Otro"):
            tk.Radiobutton(
                genero_frame, text=opcion, variable=self.genero,
                value=opcion, bg="#f4f6f8"
            ).pack(side="left", padx=3)

        tk.Checkbutton(
            frame, text="Acepto los términos y condiciones",
            variable=self.acepto, bg="#f4f6f8",
            font=("Arial", 10)
        ).grid(row=7, column=0, columnspan=2, pady=18)

        botones = tk.Frame(frame, bg="#f4f6f8")
        botones.grid(row=8, column=0, columnspan=2, pady=12)

        tk.Button(
            botones, text="Registrar", command=self.validar,
            width=15, bg="#2e8b57", fg="white",
            font=("Arial", 10, "bold")
        ).pack(side="left", padx=8, ipady=5)

        tk.Button(
            botones, text="Limpiar", command=self.limpiar,
            width=15, font=("Arial", 10)
        ).pack(side="left", padx=8, ipady=5)

        tk.Label(
            frame, text="Completa todos los campos para registrar tus datos.",
            font=("Arial", 9), fg="#555555", bg="#f4f6f8"
        ).grid(row=9, column=0, columnspan=2, pady=10)

        # Atajo de teclado: Ctrl+Enter intenta registrar.
        self.root.bind("<Control-Return>", lambda evento: self.validar())

    def validar(self):
        errores = []

        if not self.nombre.get().strip():
            errores.append("El nombre es obligatorio")

        email = self.email.get().strip()
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            errores.append("Email inválido (debe contener @ y dominio)")

        if len(self.password.get()) < 8:
            errores.append("La contraseña debe tener mínimo 8 caracteres")

        if self.password.get() != self.confirm_pass.get():
            errores.append("Las contraseñas no coinciden")

        try:
            edad = int(self.edad.get())
            if edad < 15 or edad > 99:
                errores.append("La edad debe estar entre 15 y 99")
        except ValueError:
            errores.append("La edad debe ser un número")

        if not self.genero.get():
            errores.append("Seleccione un género")

        if not self.acepto.get():
            errores.append("Debe aceptar los términos")

        if errores:
            messagebox.showerror(
                "Errores de validación",
                "\n".join(f"• {error}" for error in errores)
            )
        else:
            messagebox.showinfo(
                "Registro exitoso",
                f"¡Bienvenido {self.nombre.get().strip()}!\n"
                f"Email: {self.email.get().strip()}"
            )

    def limpiar(self):
        for variable in (
            self.nombre, self.email, self.password,
            self.confirm_pass, self.edad, self.genero
        ):
            variable.set("")
        self.acepto.set(False)
        self.entradas[0].focus_set()


if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()
