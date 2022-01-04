public class User extends Account{
    //Constructor
    public User(String name, String document, String email, String password){
        super(name, document);
    }

    //General functions
    void printDataUser(){
        System.out.println("Document user: "+document+" Name driver: "+name+" E-mail: "
        +email+" password"+password);
    }
}
