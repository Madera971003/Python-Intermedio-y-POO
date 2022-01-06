import java.util.ArrayList;
import java.util.Map;

class UberBlack extends Car{ //extends Car: toma las variables de la clase padre
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    //Constructor
    public UberBlack(String license, Account driver, String brand, String model,
    Map<String, Map<String, Integer>> typeCarAccepted,
    ArrayList<String> seatsMaterial){
        super(license, driver); //Representa la clase padre
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}
