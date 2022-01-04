// function Car(license, driver) {
//     this.id;
//     this.license = license;
//     this.driver = driver;
//     this.passenger;
// }

// Car.prototype.printDataCar = function () {
//     console.log(this.driver)
//     console.log(this.driver.name)
//     console.log(this.driver.document)
// }
class Car{

    //Constructor
    constructor(license, driver){
        this.id;
        this.license = license;
        this.driver = driver;
        this.passenger;
    }

    //General functions
    printDataCar(){
        if (this.passenger != null) {
            console.log(this.driver)
            console.log(this.license)
            console.log(this.driver.name)
            console.log(this.driver.document)
        }        
    }

    //Getters and Setters

    setPassenger(passenger) {
        if (passenger == 4) {
            this.passenger = passenger;
        }else{
            console.log("Necesitas asignar 4 pasajeros");
        }
    }

}