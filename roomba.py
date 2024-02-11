import tkinter as tk

def calcular_area():
    largo_habitacion = float(entry_largo_habitacion.get())
    ancho_habitacion = float(entry_ancho_habitacion.get())
    area_habitacion = largo_habitacion * ancho_habitacion

    largo_objeto = float(entry_largo_objeto.get())
    ancho_objeto = float(entry_ancho_objeto.get())
    area_objeto = largo_objeto * ancho_objeto

    area_limpiar = area_habitacion - area_objeto

    tiempo_limpiar_minutos = area_limpiar / velocidad_limpieza

    resultado_area_habitacion.config(text=f"Área de la habitación: {area_habitacion:.2f} metros cuadrados")
    resultado_area_limpiar.config(text=f"Área para limpiar: {area_limpiar:.2f} metros cuadrados")
    resultado_tiempo.config(text=f"Tiempo de limpieza estimado: {tiempo_limpiar_minutos:.2f} minutos")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Robot Aspirador")

# Creación de marco para controles
marco_controles = tk.Frame(ventana)
marco_controles.pack(padx=10, pady=10)

# Etiquetas y campos de entrada para dimensiones de la habitación
tk.Label(marco_controles, text="Dimensiones de la habitación:").grid(row=0, column=0, columnspan=2, padx=5, pady=5)
tk.Label(marco_controles, text="Largo (metros):").grid(row=1, column=0, padx=5, pady=5)
entry_largo_habitacion = tk.Entry(marco_controles)
entry_largo_habitacion.grid(row=1, column=1, padx=5, pady=5)
tk.Label(marco_controles, text="Ancho (metros):").grid(row=2, column=0, padx=5, pady=5)
entry_ancho_habitacion = tk.Entry(marco_controles)
entry_ancho_habitacion.grid(row=2, column=1, padx=5, pady=5)

# Etiquetas y campos de entrada para dimensiones del objeto
tk.Label(marco_controles, text="Dimensiones del objeto:").grid(row=3, column=0, columnspan=2, padx=5, pady=5)
tk.Label(marco_controles, text="Largo (metros):").grid(row=4, column=0, padx=5, pady=5)
entry_largo_objeto = tk.Entry(marco_controles)
entry_largo_objeto.grid(row=4, column=1, padx=5, pady=5)
tk.Label(marco_controles, text="Ancho (metros):").grid(row=5, column=0, padx=5, pady=5)
entry_ancho_objeto = tk.Entry(marco_controles)
entry_ancho_objeto.grid(row=5, column=1, padx=5, pady=5)

# Botón para calcular el área
boton_calcular = tk.Button(marco_controles, text="Calcular Área y Tiempo de Limpieza", command=calcular_area)
boton_calcular.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Creación de marco para mostrar resultados
marco_resultados = tk.Frame(ventana)
marco_resultados.pack(padx=10, pady=10)

resultado_area_habitacion = tk.Label(marco_resultados, text="")
resultado_area_habitacion.pack(padx=5, pady=2)

resultado_area_limpiar = tk.Label(marco_resultados, text="")
resultado_area_limpiar.pack(padx=5, pady=2)

resultado_tiempo = tk.Label(marco_resultados, text="")
resultado_tiempo.pack(padx=5, pady=2)

# Velocidad de limpieza en metros cuadrados por minuto
velocidad_limpieza = 3  # Supongamos que la aspiradora limpia 3 metros cuadrados por minuto

ventana.mainloop()
