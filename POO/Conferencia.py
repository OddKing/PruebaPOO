from Sala import Sala
from Relator import Relator
from Participante import Paticipante

class Conferencia:
    __idConferencia=None
    __relator=None
    __sala=None
    __fecha=""
    __hora=None
    __particiepantes=list()

    def __init__(self,id,realor,sala,fecha,hora):
        self.__idConferencia=id
        self.__relator=realor
        self.__sala=sala
        self.__fecha=fecha
        self.__hora=hora

    
    def getIdConferencia(self):
        return self.__idConferencia
    
    def getRelator(self):
        return self.__relator
    
    def getSala(self):
        return self.__sala
    
    def getHora(self):
        return self.__hora
    
    def getParticipantes(self):
        return self.__particiepantes
    
    def setIdConferencia(self,id):
        self.__idConferencia=id
    
    def setRelator(self,rela):
        self.__relator=rela
    
    def setSala(self,sala):
        self.__sala=sala
    
    def setFecha(self,fecha):
        self.__fecha=fecha

    def setHora(self,hora):
        self.__hora=hora

    def setParticipante(self, part):
        self.__particiepantes.append(part)

    def CambiarRealtor(self, newrealtor):
        self.__relator=newrealtor
        print("se cambio el relator")

    def CambiarSala(self, sala):
        self.__sala=sala
        print("se cambio la sala de reuniones")

    def ListarParticipantes(self):
        for pa in self.__particiepantes:
            print(pa)
