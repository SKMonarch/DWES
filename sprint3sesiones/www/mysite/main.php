<?php
	// Conexión a la base de datos 'web_juegos'
	$db = mysqli_connect('localhost','root','1234','web_juegos') or die('Fail');
?>
 
<html>
<head>
    <style>
        
        body {
            background-color: #333; 
            color: white; 
            font-family: Arial, sans-serif; 
            text-align: center; 
        }
        h1 {
            font-size: 2em; 
        }
        img {
            width: 200px; 
            height: auto; 
            margin: 10px; 
        }
		ul{
			list-style: none; 
		}
    </style>
</head>
<body>
<h1>Conexión establecida</h1>
<?php
	// Consulta SQL para obtener todos los juegos
	$query = 'SELECT * FROM tJuegos';
	$result = mysqli_query($db,$query) or die ('Query Fail');
	
	// Iteramos sobre los resultados
	while ($row = mysqli_fetch_array($result)){
		// Mostramos la imagen del juego
		echo '<img src="'.$row[2].'">';
		echo '<br>';
		// Enlace a los detalles del juego
		echo '<a href="details.php?id='. $row['id'].'"> Ver Detalles</a>';
		echo '<br>';
		// Nombre del juego
		echo '<h1>'.$row[1].'</h1>';
		echo '<br>';
		// Detalles adicionales del juego
		echo '<ul>';
		echo '<li>'.$row[3].'</li>'; // Detalle 1
		echo '<br>';
		echo '<li>'.$row[4].'</li>'; // Detalle 2
		echo '</ul>';
		echo '<br>';
	}
	// Cerramos la conexión a la base de datos
	mysqli_close($db);
?>	
</body>
</html>
