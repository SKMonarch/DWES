<?php
// Conexión a la base de datos 'web_juegos'
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail');

if (!isset($_GET['id'])) {
    die('No se ha especificado un juego'); // Verifica que se pase un ID de juego
}

$juegos_id = $_GET['id']; // Obtiene el ID del juego de la URL
$query = 'SELECT * FROM tJuegos WHERE id=' . $juegos_id; // Consulta para obtener detalles del juego
$result = mysqli_query($db, $query) or die('Query error'); // Ejecuta la consulta
$juego = mysqli_fetch_array($result); // Obtiene el resultado

// Muestra el nombre, fecha y imagen del juego
echo '<h1>' . $juego['nombre'] . '</h1>';
echo '<h2>' . $juego['fecha_lanzamiento'] . '</h2>';
echo '<img src="' . $juego['url_imagen'] . '">';

// Sección de comentarios
?>
<h3>Comentarios:</h3>
<ul>
<?php
$query2 = 'SELECT * FROM tComentarios WHERE id=' . $juegos_id; // Consulta para obtener comentarios
$result2 = mysqli_query($db, $query2) or die('Query error'); // Ejecuta la consulta

while ($row = mysqli_fetch_array($result2)) {
    echo '<li>' . $row['comentario'] . '</li>'; // Muestra cada comentario
}

mysqli_close($db); // Cierra la conexión
?>
</ul>

<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
    <textarea rows="4" cols="50" name="new_comment"></textarea><br>
    <input type="hidden" name="juegos_id" value="<?php echo $juegos_id; ?>"> <!-- ID del juego oculto -->
    <input type="submit" value="Comentar"> <!-- Botón para enviar -->
</form>

<h3>Comentarios:</h3>
<ul>
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail'); // Reconexión a la base de datos

$query2 = 'SELECT * FROM tComentarios WHERE juego_id=' . $juegos_id; // Consulta para obtener comentarios
$result2 = mysqli_query($db, $query2) or die('Query error'); // Ejecuta la consulta

while ($row = mysqli_fetch_array($result2)) {
    echo '<li>' . $row['comentario'] . ' - <small>' . $row['fecha'] . '</small></li>'; // Muestra cada comentario con fecha
}

mysqli_close($db); // Cierra la conexión
?>
</ul>
