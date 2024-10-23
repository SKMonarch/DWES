<?php
$db = mysqli_connect('localhost', 'root', '1234', 'web_juegos') or die('Fail');
?>
<html>
    <head>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        h1, h2 {
            color: #00FF00;
        }

        img {
            max-width: 300px;
            height: auto;
            border: 2px solid #00FF00;
        }
    </style>
    </head>
<body>
<?php
if (!isset($_GET['id'])) {
die('No se ha especificado un juego');
}
$juegos_id = $_GET['id'];
$query = 'SELECT * FROM tJuegos WHERE id='.$juegos_id;
$result = mysqli_query($db, $query) or die('Query error');
$juego= mysqli_fetch_array($result);
echo '<h1>'.$juego['nombre'].'</h1>';
echo '<h2>'.$juego['fecha_lanzamiento'].'</h2>';
echo '<img src="'.$juego['url_imagen'].'">';
?>
<h3>Comentarios:</h3>
<ul>
<?php
$query2 = 'SELECT * FROM tComentarios WHERE id='.$juegos_id;
$result2 = mysqli_query($db, $query2) or die('Query error');
while ($row = mysqli_fetch_array($result2)) {
echo '<li>'.$row['comentario'].'</li>';
}
mysqli_close($db);
?>
</ul>
<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
<textarea rows="4" cols="50" name="new_comment"></textarea><br>
<input type="hidden" name="cancion_id" value="<?php echo $juegos_id; ?>">
<input type="submit" value="Comentar">
</form>
</body>
</html>