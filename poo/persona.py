class Persona:
   #utiliza argumentos por defecto
    def __init__(self,nombre,apellido,edad,dni):

       self.nombre=nombre
       self.apellido=apellido
       self.edad=edad
       self.dni=dni

    def __str__(self):

       return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

    def esMayorDeEdad(self):
       return self.edad >= 18

    def apellidoVocal(self):
       return self.apellido[0] in ('A','E','I','O','U')

