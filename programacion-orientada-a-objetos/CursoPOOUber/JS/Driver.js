class Driver extends Account{
    //Constructor
    constructor(name, document){
        super(name, document)
    }

    //General functions
    printDataDriver(){
        console.log("El nombre del conductor es: "+this.name)
        console.log(this.document)
    }
}