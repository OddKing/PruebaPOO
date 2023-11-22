from datetime import date

class Persona:
    __id=None
    __nombre=""
    __fechaNacimiento=None

    def __init__(self,id,nombre,fecha):
        self.__id=id
        self.__nombre=nombre
        self.__fechaNacimiento=fecha
    

    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def setId(self,nuevoID):
        self.__id=nuevoID
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setFechaNacimiento(self,fecha):
        self.__fechaNacimiento=fecha

    def calcularEdad(self):
        hoy=date.today()
        edad=hoy.year - self.__fechaNacimiento.year - ((hoy.month,hoy.day)<(self.__fechaNacimiento.month,self.__fechaNacimiento.day))
        return edad
    
    def __str__(self):
        return "Id: {} - Nombre: {} - FechaNacimiento: {} - Edad: {} ".format(self.__id,self.__nombre,self.__fechaNacimiento,self.calcularEdad())