<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>feedback_tema4</title>
    <style>
        h1{
            text-align: center;
        }
        table {
            width: 60%;
            border-collapse:separate;
            margin: 20px auto; 
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th{
            background-color: gainsboro;
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
    <p align="center"><b>CRUD: Create, Read, Update, Select de la tabla Country de Sakila</b></p>
    <?php
        include("conexionBBDD.php");
        //LEER
        $conexion = $base->query("SELECT * FROM COUNTRY");
        $registros = $conexion->fetchAll(PDO::FETCH_OBJ);
       
        if (isset($_POST["cr"])) {
            $country = $_POST["Country"];
            $last_update = $_POST["Last_update"];
            
            //CREAR
            // Instrucción SQL con marcadores 
            $sql = "INSERT INTO COUNTRY (COUNTRY, LAST_UPDATE) VALUES (:country, :lastupdate)";
            $resultado = $base->prepare($sql);
            $resultado->execute(array(":country" => $country, ":lastupdate" => $last_update));
            
            // Para que la página actualice a sí misma
            header("Location:indexF4.php");
        }
    ?>

    <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
        <table>
            <tr>
                <th>ID</th>
                <th>Country</th>
                <th>Last_update</th>
                <th>Borrar</th>
                <th>Actualizar</th>
            </tr>

            <?php
            // buble foreach para recorrer los datos de la tabla
            foreach ($registros as $pais): 
            ?>
                <tr>
                    <td><?php echo $pais->country_id ?></td>
                    <td><?php echo $pais->country ?></td>
                    <td><?php echo $pais->last_update ?></td>
                    
                    <!-- BORRAR -->
                    <!--llamamos al formulario borrar con esta linea-->
                    <td class="bot"><a href="borrarF4.php?id=<?php echo $pais->country_id ?>">
                    <input type="button" name="del" id="del" value="Borrar"></a></td>

                    <!-- ACTUALIZAR -->
                    <!--llamamos al formulario editar con esta linea-->
                    <td><a href="editarF4.php?id=<?php echo $pais->country_id ?>&country=<?php echo $pais->country ?>&lastupdate=<?php echo $pais->last_update ?>">
                    <input type="button" name="up" id="up" value="Actualizar"></a></td>
                </tr>
            <?php
            endforeach;
            ?>
            <!--ultima linea para INSERTAR, fuera del bucle para que aparezca vacia siempre-->
            <tr>
                <td></td>
                <td><input type="text" name="Country" size="10" class="centrado"></td>
                <td><input type="text" name="Last_update" size="10" class="centrado"></td>
                <td class="bot"><input type="submit" name="cr" id="cr" value="Insertar"></td>
                <td class="sin"></td>
            </tr>
        </table>
    </form>
</body>
</html>