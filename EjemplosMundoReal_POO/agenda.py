import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Para seleccionar fechas

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Agenda Personal")

# Crear un Frame para la lista de eventos
frame_eventos = tk.Frame(root)
frame_eventos.pack(side="top", fill="both", expand=True)

# Crear un Treeview para mostrar los eventos
tree = ttk.Treeview(frame_eventos, columns=("fecha", "hora", "descripcion"))
tree.heading("fecha", text="Fecha")
tree.heading("hora", text="Hora")
tree.heading("descripcion", text="Descripción")
tree.pack(side="left", fill="both", expand=True)

# Crear un Frame para los controles de entrada y botones
frame_controles = tk.Frame(root)
frame_controles.pack(side="bottom")

# Campos de entrada
fecha_entry = DateEntry(frame_controles)
hora_entry = tk.Entry(frame_controles)
descripcion_entry = tk.Text(frame_controles, height=2)

# Etiquetas
fecha_label = tk.Label(frame_controles, text="Fecha:")
hora_label = tk.Label(frame_controles, text="Hora:")
descripcion_label = tk.Label(frame_controles, text="Descripción:")

# Empaquetar los elementos
fecha_label.pack()
fecha_entry.pack()
hora_label.pack()
hora_entry.pack()
descripcion_label.pack()
descripcion_entry.pack()


# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get("1.0", "end-1c")
    tree.insert("", "end", values=(fecha, hora, descripcion))
    # Aquí puedes agregar lógica para guardar los datos en un archivo o base de datos

# Función para eliminar un evento seleccionado
def eliminar_evento():
    item_seleccionado = tree.selection()
    if item_seleccionado:
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
            tree.delete(item_seleccionado)
            # Aquí puedes agregar lógica para eliminar los datos del archivo o base de datos

# Función para editar un evento
def editar_evento():
    item_seleccionado = tree.selection()
    if item_seleccionado:
        # Obtener los datos del evento seleccionado
        item = tree.item(item_seleccionado)
        fecha, hora, descripcion = item['values']

        # Mostrar los datos en los campos de entrada
        fecha_entry.delete(0, tk.END)
        fecha_entry.insert(0, fecha)
        hora_entry.delete(0, tk.END)
        hora_entry.insert(0, hora)
        descripcion_entry.delete('1.0', tk.END)
        descripcion_entry.insert('1.0', descripcion)

        # Crear un nuevo botón para guardar los cambios
        btn_guardar = tk.Button(frame_controles, text="Guardar Cambios", command=lambda: guardar_cambios(item_seleccionado))
        btn_guardar.pack(side="left")

        # Función para guardar los cambios
        def guardar_cambios(item):
            nueva_fecha = fecha_entry.get()
            nueva_hora = hora_entry.get()
            nueva_descripcion = descripcion_entry.get("1.0", "end-1c")
            tree.item(item, values=(nueva_fecha, nueva_hora, nueva_descripcion))
            # Aquí puedes agregar lógica para actualizar los datos en el archivo o base de datos
            btn_guardar.pack_forget()  # Eliminar el botón después de guardar
# Botones
btn_agregar = tk.Button(frame_controles, text="Agregar Evento", command=agregar_evento)
btn_eliminar = tk.Button(frame_controles, text="Eliminar Evento", command=eliminar_evento)
btn_editar = tk.Button(frame_controles, text="Editar Evento", command=editar_evento)
btn_salir = tk.Button(frame_controles, text="Salir", command=root.quit)
btn_agregar.pack(side="left")
btn_eliminar.pack(side="left")
btn_editar.pack(side="left")
btn_salir.pack(side="left")
# Ejecutar la aplicación
root.mainloop()