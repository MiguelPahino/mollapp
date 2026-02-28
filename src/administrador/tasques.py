class Tasques():

    def __init__(self):
        self.tareas = []
        self.target = None

    def getTasques(self):
        return self.tareas
    
    def getTarget(self):
        return self.target
    
    def setTarget(self,target):
        self.target = target

    def addTarea(self,tarea):
        self.tareas.append(tarea)

    def ejecucion(self,id):
        for tarea in self.tareas:
            tarea.ejecucion(id)

        self.target.ejecucion(id)
            






