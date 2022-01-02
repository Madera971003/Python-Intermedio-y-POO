<?php
class Account {
    public $idr;
    public $name;
    public $document;
    public $email;
    public $password;

    public function __construct($name, $document) {
        $this->name = $name;
        $this->document = $document;
    }
}
?>