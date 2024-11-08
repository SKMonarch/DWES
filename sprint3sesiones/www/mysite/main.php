<?php
	// Conexión a la base de datos 'web_juegos'
	$db = mysqli_connect('localhost','root','1234','web_juegos') or die('Fail');
?>
 
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Juegos</title>
    <style>
        body {
            background-color: #333; 
            color: white; 
            font-family: Arial, sans-serif; 
            text-align: center; 
        }
        h1 {
            font-size: 2em; 
            color: #ffcc00;
        }
        .lista-juegos {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            padding: 20px;
        }
        .card {
            background-color: #444;
            border-radius: 8px;
            padding: 20px;
            width: 250px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, opacity 0.3s ease;
            opacity: 0.9;
        }
        .card:hover {
            transform: scale(1.05);
            opacity: 1;
            background-color: #555;
        }
        img {
            width: 100%;
            height: auto;
            border-radius: 8px;
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

<div class="header">
    <button onclick="window.location.href='cambiarContraseña.html'">Cambiar Contraseña</button>
    <button onclick="window.location.href='register.html'">Registrarse</button>
    <button onclick="window.location.href='login.html'">Iniciar Sesión</button>
    <button onclick="window.location.href='logout.php'">Cerrar Sesión</button>
</div>

<h1>Lista de Juegos</h1>
<div class="lista-juegos">
<?php
	$query = 'SELECT * FROM tJuegos';
	$result = mysqli_query($db, $query) or die('Query Fail');
	
	while ($row = mysqli_fetch_array($result)){
		echo '<div class="card">';
		echo '<img src="' . htmlspecialchars($row['url_imagen']) . '" alt="Imagen del Juego">';
		echo '<h2>' . htmlspecialchars($row['nombre']) . '</h2>';
		echo '<p>Fecha de lanzamiento: ' . htmlspecialchars($row['fecha_lanzamiento']) . '</p>';
		echo '<p>Género: ' . htmlspecialchars($row['genero']) . '</p>';
		echo '<a href="details.php?id=' . $row['id'] . '">Ver Detalles</a>';
		echo '</div>';
	}
	mysqli_close($db);
?>	
</div>
</body>
</html>
