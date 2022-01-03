
class UberX extends Car{
    String brand;
    String model;
    //Contructor
    public UberX(String license, Account driver, String brand, String model){
        super(license, driver); //Representa la superclase
        this.brand = brand;
        this.model = model;
    }


    //General functions
    @Override
    void printDataCar() {
        // TODO Auto-generated method stub
        System.out.println("Model: " + model + ", brand " + brand);
    }
}
