from Persona import *
# se hace la herencia desde persona hacia relator para que compartan atributos y metodos.

class Relator(Persona):
    __correo=None
    __areaEstudio=""
    __idioma="Español"

    def __init__(self, id,nombre,fecha,correo,area,idioma):
        super().__init__(id,nombre,fecha)
        self.__correo=correo
        self.__areaEstudio=area
        self.__idioma=idioma


    def getCorreo(self):
        return self.__correo
    
    def getAreaEstudio(self):
        return self.__areaEstudio

    def getIdioma(self):
        return self.__idioma
    
    def setCorreo(self,correo):
        self.__correo=correo

    def setAreaEstudio(self , area):
        self.__areaEstudio=area
    
    def setIdioma(self, idioma):
        self.__idioma
    
#a=Relator(1,"carlos campaña","12-05-1993","carlos.campana.d@gmail.com","informatica","Español")
