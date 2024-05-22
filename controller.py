import tkinter as tk
from tkinter import messagebox, simpledialog
from model import ModeloListaDeTareas
from view import VistaListaDeTareas

class ControladorListaDeTareas:
    def __init__(self, root):
        self.modelo = ModeloListaDeTareas()
        self.vista = VistaListaDeTareas(root, self)
        self.vista.mostrar_tareas(self.modelo.tareas)

    def agregar_tarea(self):
        if len(self.modelo.tareas) >= 24:
            self.vista.mostrar_advertencia("No se pueden agregar más de 24 tareas.")
            return
        
        
        tarea_texto = self.vista.obtener_texto_tarea()
        if tarea_texto:
            self.modelo.agregar_tarea(tarea_texto)
            self.vista.mostrar_tareas(self.modelo.tareas)
            self.vista.limpiar_entrada_tarea()
        else:
            self.vista.mostrar_advertencia("Por favor, ingresa una tarea")

    def borrar_tarea(self):
        tarea_seleccionada = self.vista.obtener_tarea_seleccionada()
        if tarea_seleccionada:
            self.modelo.borrar_tarea(tarea_seleccionada)
            self.vista.mostrar_tareas(self.modelo.tareas)
        else:
            self.vista.mostrar_advertencia("Por favor, selecciona una tarea para borrar.")

    def editar_tarea(self):
        tarea_seleccionada = self.vista.obtener_tarea_seleccionada()
        if tarea_seleccionada:
            nuevo_texto = simpledialog.askstring("Editar Tarea", "Nuevo texto de la tarea:", parent=self.vista.root)
            if nuevo_texto:
                self.modelo.editar_tarea(tarea_seleccionada, nuevo_texto)
                self.vista.mostrar_tareas(self.modelo.tareas)
        else:
            self.vista.mostrar_advertencia("Por favor, selecciona una tarea para editar.")

    def borrar_lista(self):
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres borrar toda la lista?")
        if confirmar:
            self.modelo.borrar_lista()
            self.vista.mostrar_tareas(self.modelo.tareas)

    def guardar_lista(self):
        self.modelo.guardar_tareas()

if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorListaDeTareas(root)
    root.mainloop()

#Instalación de PyInstaller: Si aún no tienes PyInstaller instalado, puedes instalarlo utilizando pip:

#pip install pyinstaller
#Crear el archivo ejecutable: Navega al directorio donde se encuentra tu script principal de Python (el archivo .py que contiene tu aplicación) 
# en la línea de comandos y ejecuta el siguiente comando:

#pyinstaller --onefile --windowed tu_script.py
#Reemplaza tu_script.py con el nombre de tu archivo Python principal.
#Resultado: PyInstaller generará una carpeta dist en el mismo directorio que contiene el archivo ejecutable de tu aplicación. 
# Este archivo ejecutable se puede compartir y ejecutar en sistemas que no tienen Python instalado.
