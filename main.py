from src.clients.mollapp import Mollapp

from src.administrador.programadorTasques import ProgramadorTasques

from src.filtres.autontecicacion import Autenticacion
from src.filtres.autorizacion import Autorizacion

from src.targets.vehicle import Vehicle

id = input("Dinos tu nombre: ")

target = Vehicle()
programadorTasques = ProgramadorTasques(target)

programadorTasques.setTasca(Autenticacion())
programadorTasques.setTasca(Autorizacion())

mollapp = Mollapp()
mollapp.setProgramadorTasques(programadorTasques)
mollapp.enviar(id)
