import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from ttkthemes import ThemedStyle



class VistaListaDeTareas:
    def __init__(self, root, controlador):
        self.root = root
        self.root.title("Lista de Tareas")
        self.bg_color = "#FFB6C1"
        self.root.configure(bg=self.bg_color)
        self.controlador = controlador
        
        # Configurar el grid para que sea responsivo
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Crear un estilo temático
        style = ThemedStyle(root)
        style.set_theme("xpnative")
        style.configure("TButton", foreground="#FF00FF", background="#FF00FF", font=("Sobiscuit", 12), borderwidth=10, cursor="hand2")
        style.configure("TFrame")
        
        
        
        self.label_titulo = tk.Label(root, text="Lista de Tareas", font=("Sobiscuit", 16), bg=self.bg_color)
        self.label_titulo.pack(pady=(10, 5))
        
        self.label_titulo = tk.Label(root, text="Ingresa tus tareas", font=("Sobiscuit", 10), bg=self.bg_color)
        self.label_titulo.pack(pady=(10, 1))
        self.entry_tarea = ttk.Entry(root, font=("Baguet Script", 10), width=40)
        self.entry_tarea.pack(padx=20, pady=20)
       


        self.frame_botones = tk.Frame(root, bg=self.bg_color)
        self.frame_botones.pack(pady=5)
        
        #Los input se ingresan con la tecla Enter, igualmente se puede implementar este boton 
        #self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar Tarea", command=self.controlador.agregar_tarea)
        #self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_borrar = ttk.Button(self.frame_botones, text="Borrar Tarea", command=self.controlador.borrar_tarea)
        self.btn_borrar.pack(side=tk.LEFT, padx=5)

        self.btn_editar = ttk.Button(self.frame_botones, text="Editar Tarea", command=self.controlador.editar_tarea)
        self.btn_editar.pack(side=tk.LEFT, padx=5)
        
        self.btn_borrar_lista = ttk.Button(self.frame_botones, text="Borrar Lista", command=self.controlador.borrar_lista)
        self.btn_borrar_lista.pack(side=tk.LEFT, padx=5)

        self.btn_guardar = ttk.Button(self.frame_botones, text="Guardar Lista", command=self.controlador.guardar_lista)
        self.btn_guardar.pack(side=tk.LEFT, padx=5)

        self.frame_tareas = tk.Frame(root, bg=self.bg_color)
        self.frame_tareas.pack(fill=tk.BOTH, expand=True)

        self.checkboxes = []

        # Vincular la tecla "Enter" con la función agregar_tarea()
        self.root.bind("<Return>", lambda event: self.controlador.agregar_tarea())
        # Vincular el evento de cierre de la ventana con la función guardar_lista()
        self.root.protocol("WM_DELETE_WINDOW", self.controlador.guardar_lista())

    def obtener_texto_tarea(self):
        return self.entry_tarea.get()

    def limpiar_entrada_tarea(self):
        self.entry_tarea.delete(0, tk.END)

    def mostrar_advertencia(self, mensaje):
        messagebox.showwarning("Advertencia", mensaje)

    def mostrar_tareas(self, tareas):
        # Limpiar las tareas anteriores
        for _, checkbox, _ in self.checkboxes:
            checkbox.destroy()
        self.checkboxes.clear()

        # Mostrar las tareas actuales
        for tarea in tareas:
            checkbox_var = tk.BooleanVar()
            checkbox_var.set(False)
            checkbox = tk.Checkbutton(self.frame_tareas, text=tarea['texto'], variable=checkbox_var, bg=self.bg_color, activebackground=self.bg_color)
            checkbox.pack(anchor=tk.W)
            self.checkboxes.append((tarea, checkbox, checkbox_var))

    def obtener_tarea_seleccionada(self):
        for tarea, _, checkbox_var in self.checkboxes:
            if checkbox_var.get():
                return tarea
        return None
