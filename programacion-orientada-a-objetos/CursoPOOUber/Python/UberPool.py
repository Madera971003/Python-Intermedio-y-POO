from car import Car

class UberPool(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model): #Datos obligatorios para que existe el objeto
        super().__init__(license, driver)
        self.brand = brand
        self.model = model