class lapiz:
    color="amarillo"
    tieneborrador= False
    tienegarfito= True
    
    
    def dibujar(self):
        print("El lapiz esta escribiendo")
    
    
    def borrar(self):
        if self.esvalidoparaborrar():
        	print ("El lapiz esta escribiendo")
        else:
            print("No se puede borrar")
        
        
        def esvalidoparaborrar(self):
        	return self.tieneborrador

lapiz=lapiz()
lapiz.escrib()
lapiz.tieneborrador=True
lapiz.borrar()       
