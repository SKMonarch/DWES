<?php
// Conexión a la base de datos 'web_juegos'
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Error de conexión a la base de datos');

// Inicia la sesión para comprobar si hay un usuario logueado
session_start();
$user_id_a_insertar = 'NULL'; // Por defecto, el comentario será anónimo

// Verifica si hay un usuario logueado y obtiene su ID
if (!empty($_SESSION['user_id'])) {
    $user_id_a_insertar = $_SESSION['user_id'];
}

// Verifica que el formulario se haya enviado mediante el método POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Comprueba que se han recibido el ID del juego y el nuevo comentario
    if (isset($_POST['juegos_id']) && isset($_POST['new_comment'])) {
        $juegos_id = intval($_POST['juegos_id']); // Asegura que el ID sea un entero
        $comentario = mysqli_real_escape_string($db, $_POST['new_comment']); // Escapa el comentario

        // Prepara la consulta para insertar el nuevo comentario, incluyendo el usuario_id si está disponible
        $query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('$comentario', $juegos_id, $user_id_a_insertar)";
       
        // Ejecuta la consulta y verifica si se inserta correctamente
        if (mysqli_query($db, $query)) {
            echo "<p>Nuevo comentario " . mysqli_insert_id($db) . " añadido</p>"; // Muestra el ID del nuevo comentario
        } else {
            die('Error: ' . mysqli_error($db)); // Muestra un mensaje de error si la consulta falla
        }

        // Enlace para volver a la página de detalles del juego
        echo "<a href='/details.php?id=" . $juegos_id . "'>Volver</a>";
    } else {
        echo "<p>No se han proporcionado los datos del comentario.</p>"; // Mensaje si faltan datos
    }
} else {
    echo "<p>Acceso no permitido.</p>"; // Mensaje si no se accede mediante POST
}

// Cierra la conexión a la base de datos
mysqli_close($db);
?>

