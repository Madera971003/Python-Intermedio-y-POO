<?php
require_once("Car.php");
require_once("UberX.php");
require_once("UberPool.php");
require_once("UberVan.php");
require_once("Account.php");

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();

$uberPool = new UberPool("TYU567", new Account("Andrea Ferran", "ANDA765"), "Dodge", "Attitude");
$uberPool->setPassenger(4);
$uberPool->printDataCar();

$uberVan = new UberVan("OKN452", new Account("Raúl Ramírez", "RRA12"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->PrintDataCar();
?>