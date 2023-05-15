<head>
    <?php include ('header.php') ?>
</head>
<?php include("init.php");?>

<!DOCTYPE html>
<html>
<body>
<div class="container">
<?php

$file = fopen("..\Portfolio-Tracker-master\Daily Data\Portfolio\Portfolio Daily Prices.csv","r");

echo '<table id="mytable">';
  $countC=0;
  $countR=0;
  $dataR='na';
while(! feof($file))
  {
  	$countC+=1;
  //print_r(fgetcsv($file));
  $a = array(fgetcsv($file));

 	if(feof($file))
	{
		echo '</tbody>';
	}else{
 	/*if($countC==1){
 		echo '<thead>';
 			for($i=0;$i<sizeof($a[0]);$i++){
  			echo '<th>';
  			print($a[0][$i]);
  			echo '</th>';
			}
		echo'</thead><tbody>';
 	}else{
 		echo '<tr>';
  		for($i=0;$i<sizeof($a[0]);$i++){
  			echo '<td>';
  			print($a[0][$i]);
  			echo '</td>';
		}
		echo '</tr>';
	}*/
	if($countC==1){
 		echo '<thead>';
 			for($i=0;$i<sizeof($a[0]);$i++){
 				$dataR=$a[0][$countR];
 				if($dataR=='Date'){
  				echo '<th>';
  				print($a[0][$countR]);
  				echo '</th>';
				}
 				if($dataR==strtoupper($_GET['code'])){
  				echo '<th>';
  				print($a[0][$countR]);
  				echo '</th>';
  				break;
  				}else{
				$countR+=1;
				}
			}

		echo'</thead><tbody>';
 	}else{
 		echo '<tr>';
 		for($i=0;$i<sizeof($a[0]);$i++){
  			echo '<td>';
  			print($a[0][0]);
  			echo '</td>';
  			break;
		}
  		for($i=0;$i<sizeof($a[0]);$i++){
  			echo '<td>';
  			print($a[0][$countR]);
  			echo '</td>';
  			break;
		}
		echo '</tr>';
	}
	}

  }


echo '</table>';
fclose($file);
?>
</div>


</body>
</html>
