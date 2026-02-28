from .tasques import Tasques

class ProgramadorTasques:

    def __init__(self,target):
        self.tasques = Tasques()
        self.tasques.setTarget(target)
        
    def getTasques(self):
        return self.tasques.tareas
    
    def setTasca(self,tarea):
        self.tasques.addTarea(tarea)

    def ejecucionTasques(self,id):
        self.tasques.ejecucion(id)
