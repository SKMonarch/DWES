<html>
<body>
<h1> Jubilación</h1>

<?php
$primo = 7;

function edad_en_X_años($edad, $primo) {
    // Suma la edad actual con el valor de $primo
    return $edad + $primo;
}

function mensaje($age, $primo) {
    // Corrige la estructura y añade llaves
    if(edad_en_X_años($age, $primo) > 65) {
        return "En $primo años tendrás edad de jubilación";
    } else {
        return "¡Disfruta de tu tiempo!";
    }
}
?>

<table border="1">
    <tr>
        <th>Edad</th>
        <th>Info</th>
    </tr>

    <?php
    $primo = 7;
    $lista = array(53, 54, 55, 56, 57);

    foreach($lista as $valor) {
        echo "<tr>";
        echo "<td>".$valor."</td>";
        echo "<td>".mensaje($valor, $primo)."</td>";
        echo "</tr>";
    }
    ?>
</table>
</body>
</html>

