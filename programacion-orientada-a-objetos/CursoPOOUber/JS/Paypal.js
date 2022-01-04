class Paypal extends Payment{

    //Constructor
    constructor(id, email){
        super(id);
        this.email = email;
    }
}