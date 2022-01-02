
class Main{
    public static void main(String[] args) {
        //System.out.println("Hola mundo!!");
        UberX uberX = new UberX("AMQ123", new Account("Andrés Herrera", "AND123"), "Chevrolet", "Sonic");
        uberX.passenger = 4;
        uberX.printDataCar();
        
        // //System.out.println("Car license: " + car.license);
        // Car car2 = new Car("JSD353", new Account("Andrea Herrera", "AND542"));
        // car2.passenger = 3;
        // car2.printDataCar();
        // //System.err.println("Car license: " + car2.license);
    }
}