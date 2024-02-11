import tkinter as tk

class RobotAspiradorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot Aspirador")

        self.marco_controles = tk.Frame(self)
        self.marco_controles.pack(padx=10, pady=10)

        self.crear_controles()
    
    def crear_controles(self):
        # Etiquetas y campos de entrada para dimensiones de la habitación
        self.label_dim_habitacion = tk.Label(self.marco_controles, text="Dimensiones de la habitación:")
        self.label_dim_habitacion.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.label_largo_habitacion = tk.Label(self.marco_controles, text="Largo (metros):")
        self.label_largo_habitacion.grid(row=1, column=0, padx=5, pady=5)
        self.entry_largo_habitacion = tk.Entry(self.marco_controles)
        self.entry_largo_habitacion.grid(row=1, column=1, padx=5, pady=5)

        self.label_ancho_habitacion = tk.Label(self.marco_controles, text="Ancho (metros):")
        self.label_ancho_habitacion.grid(row=2, column=0, padx=5, pady=5)
        self.entry_ancho_habitacion = tk.Entry(self.marco_controles)
        self.entry_ancho_habitacion.grid(row=2, column=1, padx=5, pady=5)

        # Etiquetas y campos de entrada para dimensiones del objeto
        self.label_dim_objeto = tk.Label(self.marco_controles, text="Dimensiones del objeto:")
        self.label_dim_objeto.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.label_largo_objeto = tk.Label(self.marco_controles, text="Largo (metros):")
        self.label_largo_objeto.grid(row=4, column=0, padx=5, pady=5)
        self.entry_largo_objeto = tk.Entry(self.marco_controles)
        self.entry_largo_objeto.grid(row=4, column=1, padx=5, pady=5)

        self.label_ancho_objeto = tk.Label(self.marco_controles, text="Ancho (metros):")
        self.label_ancho_objeto.grid(row=5, column=0, padx=5, pady=5)
        self.entry_ancho_objeto = tk.Entry(self.marco_controles)
        self.entry_ancho_objeto.grid(row=5, column=1, padx=5, pady=5)

        # Botón para calcular el área
        self.boton_calcular = tk.Button(self.marco_controles, text="Calcular Área y Tiempo de Limpieza", command=self.calcular_area)
        self.boton_calcular.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

        # Creación de marco para mostrar resultados
        self.marco_resultados = tk.Frame(self)
        self.marco_resultados.pack(padx=10, pady=10)

        self.resultado_area_habitacion = tk.Label(self.marco_resultados, text="")
        self.resultado_area_habitacion.pack(padx=5, pady=2)

        self.resultado_area_limpiar = tk.Label(self.marco_resultados, text="")
        self.resultado_area_limpiar.pack(padx=5, pady=2)

        self.resultado_tiempo = tk.Label(self.marco_resultados, text="")
        self.resultado_tiempo.pack(padx=5, pady=2)

    def calcular_area(self):
        largo_habitacion = float(self.entry_largo_habitacion.get())
        ancho_habitacion = float(self.entry_ancho_habitacion.get())
        area_habitacion = largo_habitacion * ancho_habitacion

        largo_objeto = float(self.entry_largo_objeto.get())
        ancho_objeto = float(self.entry_ancho_objeto.get())
        area_objeto = largo_objeto * ancho_objeto

        area_limpiar = area_habitacion - area_objeto

        tiempo_limpiar_minutos = area_limpiar / 1.5

        self.resultado_area_habitacion.config(text=f"Área de la habitación: {area_habitacion:.2f} metros cuadrados")
        self.resultado_area_limpiar.config(text=f"Área para limpiar: {area_limpiar:.2f} metros cuadrados")
        self.resultado_tiempo.config(text=f"Tiempo de limpieza estimado: {tiempo_limpiar_minutos:.2f} minutos")

if __name__ == "__main__":
    app = RobotAspiradorApp()
    app.mainloop()
