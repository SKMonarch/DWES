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
		.header {
            display: flex;
            justify-content: flex-end;
            padding: 10px;
            background-color: #f8f9fa;
            border-bottom: 1px solid #e0e0e0;
        }
        .header button {
            margin-left: 10px;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }
        .header button:hover {
            background-color: #0056b3;
        }
        .header button:active {
            background-color: #004085;
        }
    </style>
</head>
<body>
<h1>Conexión establecida</h1>

<div class="header">
    <button onclick="window.location.href='register.html'">Registrarse</button>
    <button onclick="window.location.href='login.html'">Iniciar Sesión</button>
    <button onclick="window.location.href='logout.php'">Cerrar Sesión</button>
</div>
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
