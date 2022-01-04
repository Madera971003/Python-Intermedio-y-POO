from car import Car
from account import Account
from UberBlack import UberBlack
from UberX import UberX
from UberPool import UberPool
from UberVan import UberVan

if __name__ == "__main__":
    print("Hola Mundo")
    
    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))

    uberB = UberBlack("ASJ234", Account("Abisai Antonio", "AMA97"), "Audi", "Vinilo")
    uberB.setPassenger(5)
    uberB.printDataCar(uberB)

    uberV = UberVan("JSH456", Account("Juan Martínez", "JUM587"), "Chevrolet", "Vinilo")
    uberV.setPassenger(6)
    uberV.printDataCar(uberV)
