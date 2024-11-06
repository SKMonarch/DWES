<?php
// Conexión a la base de datos 'web_juegos'
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail');

// Verifica que se pase un ID de juego
if (!isset($_GET['id'])) {
    die('No se ha especificado un juego');
}

$juegos_id = $_GET['id']; // Obtiene el ID del juego de la URL

// Consulta para obtener detalles del juego
$query = 'SELECT * FROM tJuegos WHERE id=' . intval($juegos_id);
$result = mysqli_query($db, $query) or die('Query error');
$juego = mysqli_fetch_array($result);

// Muestra el nombre, fecha y imagen del juego
echo '<h1>' . htmlspecialchars($juego['nombre']) . '</h1>';
echo '<h2>' . htmlspecialchars($juego['fecha_lanzamiento']) . '</h2>';
echo '<img src="' . htmlspecialchars($juego['url_imagen']) . '">';

// Sección de comentarios
?>
<h3>Comentarios:</h3>
<ul>
<?php
// Consulta para obtener comentarios y el nombre del usuario que los publicó
$query2 = 'SELECT c.comentario, c.fecha, u.nombre
           FROM tComentarios c
           LEFT JOIN tUsuarios u ON c.usuario_id = u.id
           WHERE c.juego_id = ' . intval($juegos_id);

$result2 = mysqli_query($db, $query2) or die('Query error');

while ($row = mysqli_fetch_array($result2)) {
    $usuario = $row['nombre'] ? htmlspecialchars($row['nombre']) : 'Anónimo';
    echo '<li><strong>' . $usuario . ':</strong> ' . htmlspecialchars($row['comentario']) . ' - <small>' . htmlspecialchars($row['fecha']) . '</small></li>';
}

mysqli_close($db);
?>
</ul>

<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
    <textarea rows="4" cols="50" name="new_comment" required></textarea><br>
    <input type="hidden" name="juegos_id" value="<?php echo htmlspecialchars($juegos_id); ?>"> <!-- ID del juego oculto -->
    <input type="submit" value="Comentar"> <!-- Botón para enviar -->
</form>