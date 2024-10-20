<html>
<body>
<h1>Conversor de longitudes</h1>
<p>Convierte de la unidad especificada a metros</p>
<p>
<?php
if (isset($_POST["funidad"]) && isset($_POST["fcantidad"])) {
    $cantidad = $_POST["fcantidad"];
    $unidad = $_POST["funidad"];

    // Validamos que la cantidad sea numérica
    if (is_numeric($cantidad)) {
        if ($unidad == "pulgada") {
            $v_metros = $cantidad * 0.0254;
            echo $cantidad . " pulgada(s) = " . $v_metros . " metro(s)";
        } elseif ($unidad == "pie") {
            $v_metros = $cantidad * 0.3048; // Conversión de pies a metros
            echo $cantidad . " pie(s) = " . $v_metros . " metro(s)";
        } else {
            echo "Unidad no soportada.";
        }
    } else {
        echo "Por favor, ingresa una cantidad válida.";
    }
}
?>
</p>
<p>Realiza una nueva conversión:</p>
<form action="/conversor2.php" method="post">
    <label for="cantidad_input">Cantidad:</label><br>
    <input type="text" id="cantidad_input" name="fcantidad" required><br>
    
    <input type="radio" id="pulgada_input" name="funidad" value="pulgada" required>
    <label for="pulgada_input">Pulgada(s)</label><br>
    
    <input type="radio" id="pie_input" name="funidad" value="pie">
    <label for="pie_input">Pie(s)</label><br>
    
    <input type="radio" id="otro_input" name="funidad" value="otro">
    <label for="otro_input">Otro</label><br>
    
    <input type="submit" value="Convertir">
</form>
</body>
</html>

