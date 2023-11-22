from Sala import Sala
from Participante import Paticipante
from Relator import Relator
from Conferencia import Conferencia
from Persona import Persona

sal1=Sala(1,"Sala Arica","Inacap primer edificio piso1")
sal2=Sala(2,"Sala Calama","Inacap Segundo Piso ")
sal3=Sala(3,"Sala Santiago","Inacap Auditorio")
sal4=Sala(4,"Sala Rancagua ","Inacap quitno Piso ")
sal5=Sala(5,"Sala Frutillar","Inacap cuarto piso edificio 2")
sal6=Sala(6,"Sala Puerto Varas","Inacap cuarto piso edificio 1")

listasala=[sal1,sal2,sal3,sal4,sal5,sal6]
listaConferencia=[]
listaRelatore=[]
ciclosinfin=True

def Menu():
    print("Hola Bienvenido a menu gestion reserva de Salas para conferencia!")
    print("Eliga su opcion: ")
    print("1.- Relatores")
    print("2.- Salas")
    print("3.- Conferencia")
    print("4.- Participantes ")
    print("5.- Salir")
    try:  
        opcion=int(input("Ingrese la opcion que requiere: "))
        if opcion>5 or opcion==0:
            raise Exception("valor no valido debe ser entre 1 - 5")
    except Exception as inst:
        print("El tipo de error es {}, el menesaje: {} ".format(type(inst),inst.args))
        print("debe poner una opcion valida de 1 - 5")
    else:
        if 1==opcion:
            MenuRelator()
        elif 2==opcion:
            MenuSalas()
        elif 3==opcion:
            MenuConferencia()
        elif 4==opcion:
            MenuParticipantes()
        elif 5==opcion:
            Salir()
    
    

def MenuRelator():
    pass

def MenuSalas():
    pass 

def MenuConferencia():
    pass

def MenuParticipantes():
    pass

def Salir():
    print("Saliendo del programa")
    global ciclosinfin
    ciclosinfin = False

while ciclosinfin:

    Menu()  
