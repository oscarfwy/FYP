<?php
//exec("python python/data.py calc_index(HSI,2020-02-01,2020-02-21)",$output);
$output = shell_exec("python python/toPHP.py");


$arr0 =explode("Date",$output);
$strp =$arr0[0];
$strc =$arr0[1];
$substrp = substr($strp, strpos($strp,'completed')+10,strpos($strp,'dtype')-strpos($strp,'completed')-10);
$substrc = substr($strc, 0 ,strpos($strc,'Name'));
$arrp =preg_split("/\s+/",$substrp);
$arrc =preg_split("/\s+/",$substrc);

$datec= array();
$ratec= array();

for ($i=0 ; $i< count($arrc)-1; $i++){

	if($i%2==0){
		array_push($ratec , $arrc[$i]);
	}else{
		array_push($datec , $arrc[$i]);
	}
}

$strratec="[";
for ($i=1 ; $i< count($ratec); $i++){
     $strratec.=$ratec[$i].",";
     if($i== count($ratec)-1){
     	$lastratec= number_format($ratec[$i],2,'.','');
     	}
     	if($i== count($ratec)-2){
     	$seclastratec=number_format($ratec[$i],2,'.','');
     	}
}
$strratec.="]";

$strdatec="[";
for ($i=0 ; $i< count($datec); $i++){
     $strdatec.="'".$datec[$i]."',";


}
$strdatec.="]";

$datep= array();
$ratep= array();

for ($i=0 ; $i< count($arrp)-1; $i++){

	if($i%2==0){
		array_push($datep , $arrp[$i]);
	}else{
		array_push($ratep , $arrp[$i]);
	}
}
$lastratep=0;
$seclastratep=0;
$strratep="[";
for ($i=0 ; $i< count($ratep); $i++){
     $strratep.=$ratep[$i].",";
     if($i== count($ratep)-1){
     	$lastratep= number_format($ratep[$i],2,'.','');
     	}
     	if($i== count($ratep)-2){
     	$seclastratep=number_format($ratep[$i],2,'.','');
     	}
}
$strratep.="]";

$strdatep="[";
for ($i=0 ; $i< count($datep); $i++){
     $strdatep.="'".$datep[$i]."',";


}
$strdatep.="]";







/*
$str1 = substr($output, strpos($output,'Date')+5,strpos($output,'Name')-strpos($output,'Date')-5);
$arr1 =preg_split("/\s+/",$str1);
$date= array();
$rate= array();
for ($i=0 ; $i< count($arr1)-1; $i++){

	if($i%2==0){
		array_push($date , $arr1[$i]);
	}else{
		array_push($rate , $arr1[$i]);
	}
}
$strrate="[";
for ($i=0 ; $i< count($rate); $i++){
     $strrate.=$rate[$i].",";
     if($i== count($rate)-1){
     	$lastrate= number_format($rate[$i],2,'.','');
     	}
     	if($i== count($rate)-2){
     	$seclastrate=number_format($rate[$i],2,'.','');
     	}
}

$strrate.="]";

$strdate="[";
for ($i=0 ; $i< count($date); $i++){
     $strdate.="'".$date[$i]."',";


}

$strdate.="]";

*/
?>