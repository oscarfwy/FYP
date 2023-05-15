
<?php
function getDataBySymbol($code,$mode) {
  $fp ="..\Portfolio-Tracker-master\Daily Data\Portfolio\Portfolio Daily Prices.csv";
if(file_exists($fp)){
  $file = fopen($fp,"r");
  $countC=0;
  $countR=0;
  $dataR='na';

while(! feof($file))
  {
    $countC+=1;
  $a[$countC] = array(fgetcsv($file));
  if(feof($file))
  {
    if($mode==0){
    if($a[$countC-1][0][$countR]==''){
      echo 'N/A';
    }else{
    echo $a[$countC-1][0][$countR];
  }
  }else if($mode==1){
    if($a[$countC-1][0][$countR]==''){
       echo '<div class="badge badge-danger">'.'N/A'.'</div>';
    }else if($a[$countC-2][0][$countR]==''){
       echo '<div class="badge badge-danger">'.'N/A'.'</div>';
    }else{
      $change= number_format((float) (1- ($a[$countC-1][0][$countR])/(($a[$countC-1][0][$countR]+$a[$countC-2][0][$countR])/2)),2,'.','');
      if($change>=0){
        echo '<div class="badge badge-success">'.number_format((float)$change,2,'.','').'%'.'</div>';
      }else{
         echo '<div class="badge badge-danger">'.number_format((float)$change,2,'.','').'%'.'</div>';
      }
         };
  }
  }else{
  if($countC==1){
    for($i=1;$i<sizeof($a[1][0]);$i++){
      $dataR=$a[$countC][0][$countR];
        if($dataR==$code){
          break;
          }else{
             $countR +=1;
        }
      }
    }
  }


  }
}
}
function getDataBySymbolN($code) {
  echo getDataBySymbol($code,0);
  }
function getDataBySymbolC($code) {
  echo getDataBySymbol($code,1);
}
?>