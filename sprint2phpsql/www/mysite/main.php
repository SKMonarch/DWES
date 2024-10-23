<?php
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
	$query = 'SELECT * FROM tJuegos';
	$result = mysqli_query($db,$query) or die ('Query Fail');
	while ($row = mysqli_fetch_array($result)){
		echo '<img src="'.$row[2].'">';
		echo '<br>';
		echo '<a href="details.php?id='. $row['id'].'"> Ver Detalles</a>';
		echo '<br>';
		echo '<h1>'.$row[1].'</h1>';
		echo '<br>';
		echo '<ul>';
		echo '<li>'.$row[3].'</li>';
		echo '<br>';
		echo '<li>'.$row[4].'</li>';
		echo '</ul>';
		echo '<br>';}
	mysqli_close($db);
?>	
</body>
</html>
