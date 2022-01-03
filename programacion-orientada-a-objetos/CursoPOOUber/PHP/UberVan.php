<?php
require_once('car.php');
class UberVan extends Car{
    public $typeCarAccepted;
    public $seatsMaterial;
    //Constructor
    public function __construct($license, $driver, $typeCarAccepted, $seatsMaterial){
        parent:: __construct($license, $driver); //Representa la superclase
        $this->typeCarAccepted  = $typeCarAccepted;
        $this->seatsMaterial = $seatsMaterial;
    }


    //Getters and Setters
    public function setPassenger($passenger){
        if($passenger == 6){
            $this->passenger = $passenger;
        }
        else{
            echo "Necesitas asignar 4 pasajeros";
        }
    }
}
?>