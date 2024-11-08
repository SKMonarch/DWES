<?php
session_start();

/
if (!isset($_SESSION['user_id'])) {
    die("Acceso denegado. Debes iniciar sesión.");
}

$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Error de conexión a la base de datos');


$current_password = $_POST['current_password'];
$new_password = $_POST['new_password'];
$confirm_password = $_POST['confirm_password'];


if ($new_password !== $confirm_password) {
    die("Las nuevas contraseñas no coinciden.");
}


$user_id = $_SESSION['user_id'];


$stmt = mysqli_prepare($db, "SELECT contraseña FROM tUsuarios WHERE id = ?");
mysqli_stmt_bind_param($stmt, "i", $user_id);
mysqli_stmt_execute($stmt);
mysqli_stmt_bind_result($stmt, $hashed_password);
mysqli_stmt_fetch($stmt);
mysqli_stmt_close($stmt);


if (!password_verify($current_password, $hashed_password)) {
    die("La contraseña actual es incorrecta.");
}


$new_hashed_password = password_hash($new_password, PASSWORD_DEFAULT);


$stmt = mysqli_prepare($db, "UPDATE tUsuarios SET contraseña = ? WHERE id = ?");
mysqli_stmt_bind_param($stmt, "si", $new_hashed_password, $user_id);
if (mysqli_stmt_execute($stmt)) {
    echo "Contraseña actualizada correctamente.";
} else {
    echo "Error al actualizar la contraseña.";
}

mysqli_stmt_close($stmt);
mysqli_close($db);
?>