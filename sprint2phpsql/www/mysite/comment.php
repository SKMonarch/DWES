<?php
// Conexión a la base de datos 'web_juegos'
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail');

// Verifica si se ha enviado un formulario mediante el método POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Comprueba que se han recibido el ID del juego y el nuevo comentario
    if (isset($_POST['juegos_id']) && isset($_POST['new_comment'])) {
        $juegos_id = $_POST['juegos_id']; // Obtiene el ID del juego
        $comentario = mysqli_real_escape_string($db, $_POST['new_comment']); // Escapa el comentario para evitar inyecciones SQL

        // Prepara la consulta para insertar el nuevo comentario en la base de datos
        $query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('$comentario', $juegos_id, NULL)";
        
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
