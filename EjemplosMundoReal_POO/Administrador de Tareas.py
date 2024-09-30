import tkinter as tk

class AdministradorAmong_Us:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Tareas")

        # Crear los elementos de la interfaz
        self.entry_task = tk.Entry(master)
        self.entry_task.pack()

        self.button_add = tk.Button(master, text="Añadir Tarea", command=self.añadir_tarea)
        self.button_add.pack()

        self.button_complete = tk.Button(master, text="Completar Tarea", command=self.completar_tarea)
        self.button_complete.pack()

        self.button_delete = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.button_delete.pack()

        self.task_list = tk.Listbox(master)
        self.task_list.pack()

        # Lista para almacenar las tareas
        self.tasks = []


    def añadir_tarea(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def completar_tarea(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_task = self.task_list.get(selected_index)
            self.task_list.delete(selected_index)
            print(f"Tarea marcada como completada: {selected_task}")

    def eliminar_tarea(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
            del self.tasks[selected_index[0]]  # Eliminar de la lista interna

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = AdministradorAmong_Us(root)
root.mainloop()