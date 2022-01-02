from _typeshed import SupportsReadline
from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial   = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial): #Datos obligatorios para que existe el objeto
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial