from Persona import *

class Paticipante(Persona):
    __correo=None
    #este es el area que pertence la persona puede ser area de empresa, o de la universidad
    __area=None

    def __init__(self,id,nombre,fecha,correo,area):
        super().__init__(id,nombre,fecha)
        self.__correo=correo
        self.__area=area

    def getCorreo(self):
        return self.__correo
    
    def getArea(self):
        return self.__area
    
    def setCorre(self,correo):
        self.__correo=correo

    def setArea(self, area):
        self.__area=area

    def __str__(self):
        return "{} Correo: {} - Area: {}".format(super().__str__(),self.__correo,self.__area)
    