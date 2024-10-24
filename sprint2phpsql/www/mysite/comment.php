<?php
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail');

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['juegos_id']) && isset($_POST['new_comment'])) {
        $juegos_id = $_POST['juegos_id'];
        $comentario = mysqli_real_escape_string($db, $_POST['new_comment']);

        $query = "INSERT INTO tComentarios (comentario, juego_id, usuario_id) VALUES ('$comentario', $juegos_id, NULL)";
        
        if (mysqli_query($db, $query)) {
            echo "<p>Nuevo comentario " . mysqli_insert_id($db) . " añadido</p>";
        } else {
            die('Error: ' . mysqli_error($db));
        }

        echo "<a href='/details.php?id=" . $juegos_id . "'>Volver</a>";
    } else {
        echo "<p>No se han proporcionado los datos del comentario.</p>";
    }
} else {
    echo "<p>Acceso no permitido.</p>";
}

mysqli_close($db);
?>
