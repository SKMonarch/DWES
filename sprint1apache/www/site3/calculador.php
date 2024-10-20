<!DOCTYPE html>
<html>
<head>
    <title>Calculadora</title>
</head>
<body>
    <h1>Calculadora</h1>
    <form method="post">
        <input type="number" name="numero1" required>
        <input type="number" name="numero2" required>
        <select name="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>
        <input type="submit" value="Calcular">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $numero1 = $_POST['numero1'];
        $numero2 = $_POST['numero2'];
        $operacion = $_POST['operacion'];
        $resultado = 0;

        switch ($operacion) {
            case 'suma':
                $resultado = $numero1 + $numero2;
                break;
            case 'resta':
                $resultado = $numero1 - $numero2;
                break;
            case 'multiplicacion':
                $resultado = $numero1 * $numero2;
                break;
            case 'division':
                if ($numero2 != 0) {
                    $resultado = $numero1 / $numero2;
                } else {
                    echo "No se puede dividir por cero.";
                    return;
                }
                break;
        }
        echo "El resultado es: $resultado";
    }
    ?>
</body>
</html>
