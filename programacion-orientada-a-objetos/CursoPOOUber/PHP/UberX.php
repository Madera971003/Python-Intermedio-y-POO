<?php
require_once('car.php');
class UberX extends Car{
    public $brand;
    public $model;

    public function __construct($license, $driver, $brand, $model){
        parent:: __construct($license, $driver); //Representa la superclase
        $this->brand  = $brand;
        $this->model = $model;
    }

    //General Functions
    public function printDataCar() {
        echo "
            Licencia: {$this->license }
            Driver: {$this->driver->name} 
            Número de pasajeros: {$this->passenger}
            Marca: {$this->brand}
            Modelo: $this->model
        ";
    }
}
?>