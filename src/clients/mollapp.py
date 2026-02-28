from src.clients.client import Client

class Mollapp(Client):

    def __init__(self):
        self.programadorTasques = None

    def setProgramadorTasques(self, programadorTasques):
        self.programadorTasques = programadorTasques
    
    def enviar(self,id):
        self.programadorTasques.ejecucionTasques(id)


        

