from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial   = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial): #Datos obligatorios para que existe el objeto
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
    
    def setPassenger(self, passenger):
        if passenger == 6:
            self.passenger = passenger
        else:
            self.passenger = None
            print("Debe asignar 6 pasajeros")