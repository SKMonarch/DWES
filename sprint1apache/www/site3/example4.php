<html>
<body>
<h1> Jbilación</h1>


<?php>

function edad_en_X_años($edad, $primo) {
	return $edad  $primo;
}


function mensaje($age, $primo)
	if(edad_en_X_años($age, $primo) >65) {
		return "En $primo años tendrás edad de jubilación";
	}else{
		return "¡Disfruta de tu tiempo!";
	}

}
?>

<table border="1">
<tr<
<th>Edad</th>
<th>Info</th>
</tr>

<?php

$numero_primo = 7;
$lista = array(53,54,55,56,57);

foreach($lista as $valor){
	echo "<tr>";
	echo "<td>.$valor."</td>";
	echo "<td>".mensaje($valor,$numero_primo)."</td>";
	echo "</tr>";
}
?>

</table>
</body>
</html>
