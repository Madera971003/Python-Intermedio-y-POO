import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car{ //la clase hija toma las var del padre
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    //Constructor
    public UberVan(String license, Account driver, String brand, String model,
    Map<String, Map<String, Integer>> typeCarAccepted,
    ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
    public UberVan(String license, Account driver) {
        super(license, driver);
    }
    

    //Getters and Setters
    @Override //Esto es polimorfismo (Se sobreescribe)
    public void setPassenger(Integer passenger) {
        // TODO Auto-generated method stub
        if(passenger == 6){
            this.passenger = passenger;
        }else{
            System.out.println("Necesitas asignar 6 pasajeros");
        }
    }
}
