from account import Account

class Car:
    id          = int
    license     = str
    driver      = Account("","")
    passenger   = int

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver
    
    def printDataCar(self, uber): #Todas las funciones deben llevar "self"
        if self.passenger is not None:
            print(vars(uber))

    def setPassenger(self, passenger):
        if passenger == 4:
            self.passenger = passenger
        else:
            self.passenger = None
            print("Debe asignar 4 pasajeros")