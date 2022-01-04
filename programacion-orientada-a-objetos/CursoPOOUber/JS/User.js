class User extends Account{
    //Constructor
    constructor(name, document){
        super(name, document)
    }

    //General functions
    printDataUser(){
        console.log("El nombre de usuario es: "+this.name)
        console.log(this.document)
    }
}