class UberVan extends Car{
    constructor(license, driver, typeCarAccepted, seatsMaterial){
        super(license, driver)
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    //General functions
    setPassenger(passenger){
        if (passenger == 6) {
            this.passenger == passenger;
        }else{
            console.log("Necesitas asignar 6 pasajeros")
        }
    }
}