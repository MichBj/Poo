import tkinter as tk


# Lista para almacenar las conversiones
historial = []
#definimos la funcion que nos permitira hacer la conversion de Longitud
def convertir():
    try:
        cm = float(entry_cm.get())
        pies = cm / 30.48
        # Agregar la conversión al historial
        historial.append(f"{cm} cm = {pies:.2f} pies")
        label_resultado.config(text=f"{cm} cm son {pies:.2f} pies")
    except ValueError:
        label_resultado.config(text="Ingrese un valor numérico válido")

def limpiar():
    entry_cm.delete(0, tk.END)
    label_resultado.config(text="")
    # Limpiar el historial
    historial.clear()


def mostrar_historial():
    # Crear una nueva ventana para mostrar el historial
    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de Conversiones")

    # Crear una lista de texto para mostrar el historial
    lista_historial = tk.Listbox(ventana_historial)
    for conversion in historial:
        lista_historial.insert(tk.END, conversion)
    lista_historial.pack()
def Salir():
    print("Hasta Luego")
    exit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Centímetros a Pies")

# Crear los elementos de la interfaz
label_cm = tk.Label(ventana, text="Ingrese los centímetros:")
entry_cm = tk.Entry(ventana)
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
label_resultado = tk.Label(ventana)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_Salir = tk.Button(ventana, text="Sali", command=Salir)
boton_historial = tk.Button(ventana, text="Ver Historial", command=mostrar_historial)
# Colocar los elementos en la ventana
label_cm.pack()
entry_cm.pack()
boton_convertir.pack()
label_resultado.pack()
boton_limpiar.pack()
boton_historial.pack()
boton_Salir.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()