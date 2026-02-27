from src.targets.vehicle import Vehicle

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

if __name__ == "__main__":

    vehicle = Vehicle()
    tasques = Tasques()
    tasques.setTarget(vehicle)
    assert tasques.getTarget is vehicle



