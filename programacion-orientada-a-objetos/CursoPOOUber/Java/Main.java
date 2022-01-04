class Main{
    public static void main(String[] args) {
        UberX uberX = new UberX("AMQ123", new Account("Andrés Herrera", "AND123"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH267", new Account("Andrés Herrera", "AND123"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();

        // Esta creacion debe estar relacionado a un usuario
        Card tarjeta = new Card(1234);
        tarjeta.setNumber(545565);
        tarjeta.setCvv(223);
        tarjeta.prinDataCard();


    }
}