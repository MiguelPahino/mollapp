from src.filtres.filtre import Filtre

class Autenticacion(Filtre):

    def ejecucion(self,id):
        print("Autenticacion OK para " + id)

if __name__ == "__main__":

    autenticacion = Autenticacion()
    autenticacion.ejecucion("Gabriel")