from car import Car
from account import Account
from UberBlack import UberBlack

if __name__ == "__main__":
    print("Hola Mundo")
    
    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))
    # uberB = UberBlack("ASJ234", Account("Abisai Antonio", "AMA97"), "Audi", "Vinilo")
    # uberB.printDataCar()
