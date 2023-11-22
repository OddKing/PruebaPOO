class Sala:
    __id=None
    __nombre=""
    __ubicacion=None

    def __init__(self,id,nombre,ubicacion):
        self.__id=id
        self.__nombre=nombre
        self.__ubicacion=ubicacion

    
    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getUbicacion(self):
        return self.__ubicacion
    
    def setId(self,id):
        self.__id=id
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setUbicacion(self,ubicacion):
        self.__ubicacion=ubicacion
        