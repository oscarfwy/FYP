<!DOCTYPE html>
<html>
<head>
	<title>Stock</title>

    <?php include ('header.php') ?>
	<?php include ('getdata.php')?>
	<?php include ('getdata.php')?>
</head>
<body class="header-fixed">
	<?php include ('nav-header.php') ?>
	<div class="page-body">
 		<?php include 'sidebar.php' ?>
 		<div class="page-content-wrapper">
			<div class="row">
				<div class="col-12">
				<p> <span class="title1">HANG SENG INDEX</span></p>
				<p> <span class="subtitle">^HSI</span><p>

				</div>
				<div class="col-12 text-left pt-2">
					<div class="row">
					<div class="col-2"><span class=" title2 stock-details"><?php echo $lastratec;?></span><span class="hkd">HKD</span></span></div>
					<div class="col-2"><span class="title2 stock-details"><?php echo $seclastratec;?></span><span class="hkd">HKD</span></div>
					<div class="col-2"></div>
					<div class="col-2"><span class="subtitle stock-details">Prediction</span></div>
					<div class="col-2"><span class="title2 stock-details"><?php echo $seclastratep;?></span><span class="hkd">HKD</span></div>
					<div class="col-2"><span class="title2 stock-details"><?php echo $seclastratep;?></span><span class="hkd">HKD</span></div>


				</div>
				</div>
				<div class="col-12 text-left pb-2">
					<div class="row">
						<div class="col-2"><span class="subtitle stock-details">Last Rate</span></div>
						<div class="col-2"><span class="subtitle stock-details">Yesterday Rate</span></div>
						<div class="col-4"></div>
						<div class="col-2"><span class="subtitle stock-details">Last Rate</span></div>
						<div class="col-2"><span class="subtitle stock-details">Yesterday Rate</span></div>


					</div>
				</div>
				<div class="col-12 py-4">
					<spam class="title3">HSI Chart</span>
				</div>
				<div class="col-12">
					    <div class="chartWrapper">
      						<div class="chartAreaWrapper">
      						  <div class="chartAreaWrapper2">
      						      <canvas id="myChart"></canvas>
      						  </div>
     						</div>

     						   <canvas id="myChartAxis" height="300" width="0"></canvas>
  						 </div>

				</div>
				</div>
			</div>

		</div>
	</div>
</body>
<?php include ('footer.php') ?>
</html>