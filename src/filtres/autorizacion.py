from filtre import Filtre

class Autorizacion(Filtre):

    def __init__(self):
        pass

    def ejecucion(self,id):
        print("Autorizacion OK para " + id)