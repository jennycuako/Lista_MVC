import json

class ModeloListaDeTareas:
    def __init__(self, archivo='tareas.json'):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open(self.archivo, 'r') as f:
                data = f.read()
                if data:
                    return json.loads(data)
        except FileNotFoundError:
            return []
        return []

    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.tareas, f)

    def agregar_tarea(self, tarea_texto):
        tarea = {'texto': tarea_texto, 'completada': False}
        self.tareas.append(tarea)
        self.guardar_tareas()

    def borrar_tarea(self, tarea):
        self.tareas.remove(tarea)
        self.guardar_tareas()

    def editar_tarea(self, tarea, nuevo_texto):
        tarea['texto'] = nuevo_texto
        self.guardar_tareas()

    def borrar_lista(self):
        self.tareas.clear()
        self.guardar_tareas()
