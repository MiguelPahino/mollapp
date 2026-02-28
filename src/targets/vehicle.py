from src.targets.target import Target

class Vehicle(Target):

    def __init__(self):
        pass

    def ejecucion(self, id):
        print("Puerta abierta " + id)