<?php
    include("conexionBBDD.php");
    //se pueden borrar solo los paises que nosotros hemos introducido, lo que viene en la BD no se pueden borrar 
    // para borrar a través de id, comprobamos si se ha pulsado borrar
    // tengo que usar $_GET["id"] : null ; por que si no me salta error
    $id = isset($_GET["id"])? $_GET["id"] : null ;
// incluyo un try catch porque al principio me daba problemas y no sabia por que 
    if ($id) {
        try {
            // si se ha pulsado y no hay ningun error hacemos la intrucción sql borrar:
            $sql = "DELETE FROM COUNTRY WHERE country_id = :id";
            $resultado = $base->prepare($sql);
            $resultado->bindParam(':id', $id, PDO::PARAM_INT);
            $resultado->execute();

            // una vez borrado, pongo este codigo para no salir de la pagina principal
            header("Location: indexF4.php");
        } catch (PDOException $e) {
            // si salta algun error se captuara 
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "No se ha podido borrar el registro ";
    }
?>