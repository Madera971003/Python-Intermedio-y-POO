import java.util.Date;


public class Card extends Payment {
    Integer number;
    Integer cvv;
    Date date;
    //Constructor
    public Card(Integer id) {
        super(id);
    }

    //General functions
    void prinDataCard(){
        if(number != null & cvv != null){
            System.out.println("El número de tarjeta es: " + number + ", con el cvv: " + cvv);
        }
    }

    //Getters and Setters
    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        String var = number+"";
        if(var.length() == 6){
            this.number = number;
        }
        else{
            System.out.println("Número de tarjeta no válida");
        }
        
    }

    public Integer getCvv() {
        return cvv;
    }

    public void setCvv(Integer cvv) {
        String var = cvv+"";
        if(var.length() == 3){
            this.cvv = cvv;
        }else{
            System.out.println("Número de cvv no válido");
        }
    }
    
}
