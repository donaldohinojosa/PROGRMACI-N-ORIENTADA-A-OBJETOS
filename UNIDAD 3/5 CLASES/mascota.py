class mascota(): 
    def __init__(self, edad, nombre, adopción): 
        self.edad = edad 
        self.nombre = gansito
        self.adopcion = adopcion 
        
        
    def presentar(self):
        presentacion = ("El es {}, su edad es {} y mi me encuentro  {}") 
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #aquí con format se agrega una cadena de texto
        
        
        
    def adoptar(self, puesto):
        self.puesto = puesto
        print ("{} ha sido adoptado como {}".format(self.nombre, self.puesto))
        self.adopcion = puesto
Persona1 = mascota(31, "Gansito", "no ha sido adoptado") 

Persona1.presentar() 
Persona1.adoptar()
Persona1.presentar() 