<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doc. actualizar</title>
    <style>
        h1{
            text-align: center;
        }
        table {
            width: 60%;
            border-collapse: separate;
            margin: 20px auto; 
        }

         td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }


        .bot {
            text-align: center;
            
            
        }

        .centrado {
            width: 100%;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <h1>ACTUALIZAR</h1>
    <?php
    //se incluye la conexcion
        include("conexionBBDD.php");
        //se hace un if/ else porque se pueden dar varios casos:
        // que solo se quiera actualizar una cosa o varias, con el GET coge los datos pasados por url y con post los datos metidos por el usuario
        if (!isset($_POST["bot_actualizar"])) {
            $id = $_GET["id"];
            $country = $_GET["country"];
            $last_update = $_GET["lastupdate"];
        } else {
            $id = $_POST["id"];
            $country = $_POST["country"];
            $last_update = $_POST["lastupdate"];
        
            //he preferido incluir htmlspecialchars() para que no pueda haber ningun ataque a la base de datos 
            $country = htmlspecialchars($country);
            $last_update = htmlspecialchars($last_update);
            try {
                // Instrucción SQL de actualizar
                // solo se podrá actualizar country y last update, el country_id es automatico y esta oculto
                $sql = "UPDATE COUNTRY SET country=:miCountry, last_update=:miLast WHERE country_id=:miID";
                $resultado = $base->prepare($sql);
                $resultado->execute(array(":miID" => $id, ":miCountry" => $country, ":miLast" => $last_update));
                header("Location:indexF4.php");
                exit();
                //captuar la expcion si hubiese
            } catch (PDOException $e) {
                // con get saltará el tipo de error que es
                echo "Error: " . $e->getMessage();
            }
        }
    ?>
    
    <p></p>    
    <p>&nbsp;</p>
    <form name="formulario1" method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">

        <table whidth="25%" border="0" align="center">
            <tr>
                <td></td>
                <td><label for="id"><input type="hidden" name="id" id="id" value="<?php echo $id ?>" ></td> <!--hiden esta oculto-->
            </tr>
            <tr>
                <td ><b>COUNTRY</b></td>
                <td><label for="nom"><input type="text" name="country" id="country" value="<?php echo $country ?>"></td>
            </tr>
            <tr>
                <td><b>LAST UPDATE</b></td>
                <td><label for="ape"><input type="text" name="lastupdate" id="lastupdate" value="<?php echo $last_update ?>"></td>
            </tr>
        
            <tr>
                <td colspan="2"><input type="submit" name="bot_actualizar" id="bot_actualizar" value="Actualizar"></td>
            </tr>

        </table>
    </form>
</body>
</html>