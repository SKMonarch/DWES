<?php
// Conectar a la base de datos usando tus credenciales
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Error de conexión a la base de datos');

// Obtener los datos del formulario
$email_posted = $_POST['email'];
$password1 = $_POST['password1'];
$password2 = $_POST['password2'];
$nombre = $_POST['nombre'];
$apellidos = $_POST['apellidos'];

// Verificar que los campos no estén vacíos y que las contraseñas coincidan
if (empty($email_posted) || empty($password1) || empty($password2) || empty($nombre) || empty($apellidos)) {
    echo '<p>Todos los campos son obligatorios</p>';
} elseif ($password1 !== $password2) {
    echo '<p>Las contraseñas no coinciden</p>';
} else {
    // Comprobar si el email ya está registrado
    $query = "SELECT id FROM tUsuarios WHERE email = '$email_posted'";
    $result = mysqli_query($db, $query) or die('Error en la consulta de verificación');

    if (mysqli_num_rows($result) > 0) {
        echo '<p>El correo ya está registrado</p>';
    } else {
        // Crear el hash de la contraseña y registrar al usuario
        $password_hashed = password_hash($password1, PASSWORD_DEFAULT);
        $query = "INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES ('$nombre', '$apellidos', '$email_posted', '$password_hashed')";
        mysqli_query($db, $query) or die('Error al insertar usuario');
       
        header('Location: main.php');
        exit();
    }
}

// Cerrar conexión
mysqli_close($db);
?>