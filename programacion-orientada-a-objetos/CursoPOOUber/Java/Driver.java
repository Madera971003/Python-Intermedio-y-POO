public class Driver extends Account{
    public Driver(String name, String document, String email, String password){
        super(name, document);
    }
    void printDataDriver(){
        System.out.println("Document driver: "+document+" Name driver: "+name+" E-mail: "
        +email+" password"+password);
    }
    
}
