
<?php

$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Error de conexión a la base de datos');

$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];

$query = "SELECT id, contraseña FROM tUsuarios WHERE email = '$email_posted'";
$result = mysqli_query($db, $query) or die('Error en la consulta de inicio de sesión');

if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);

    // Comprobar si la contraseña es correcta
    if (password_verify($password_posted, $only_row['contraseña'])) {
        session_start();
        $_SESSION['user_id'] = $only_row['id'];
        header('Location: main.php');
        exit();
    } else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}

// Cerrar conexión
mysqli_close($db);
?>