<?php
require_once('account.php');
class Car {
    public $id;
    public $license;
    public $driver;
    protected $passenger;
    //Constructor
    public function __construct($license, $driver) {
        $this->license = $license;
        $this->driver = $driver;
    }

    //General functions
    public function printDataCar() {
        echo "
            Licencia: $this->license 
            Driver: {$this->driver->name} 
            Número de pasajeros: $this->passenger\n
        ";
    }


    //Getters and Setters
    public function getPassenger(){
        return $this->passenger;
    }
    public function setPassenger($passenger){
        if($passenger == 4){
            $this->passenger = $passenger;
        }
        else{
            echo "Necesitas asignar 4 pasajeros";
        }
    }
}
?>