<script>
$(document).ready( function () {

  $('#mytable').DataTable({
    responsive: true,
    "columnDefs": [
    { "width": "100%", "targets": 0 }
  ]
});



var ctx = document.getElementById("myChart").getContext("2d");

        var chart = {
        options: {
          responsive: true,
          maintainAspectRatio: false,
          elements: {
            line: {
                tension: 0
            }
        },

          animation: {

                    onComplete: function(animation) {
                        var sourceCanvas = myLiveChart.chart.canvas;
                        var copyWidth = myLiveChart.scales['y-axis-0'].width - 10;
                        var copyHeight = myLiveChart.scales['y-axis-0'].height + myLiveChart.scales['y-axis-0'].top + 10;
                        var targetCtx = document.getElementById("myChartAxis").getContext("2d");
                        targetCtx.canvas.width = copyWidth;
                targetCtx.drawImage(sourceCanvas, 0, 0, copyWidth, copyHeight, 0, 0, copyWidth, copyHeight);
                    }
                }


      },
        type: 'line',
        data: {
            labels: <?php echo $strdatec?>,
            datasets: [
                {
                    label: "Current Rate",
                    fill: false,
                    borderDash: [2, 2],
                    borderColor: "rgba(235, 168, 52,1)",
                    pointBorderColor: "rgba(235, 162, 52,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHoverBorderColor: "rgba(235, 162, 52,1)",
                    data: <?php echo $strratec?>

                },
                {
                    label: "Predicted Rate",
                    fill: false,
                    borderDash: [2, 2],
                    borderColor: "rgba(46, 209, 228,1)",
                    pointBorderColor: "rgba(46, 209, 228,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHoverBorderColor: "rgba(46, 209, 228,1)",
                    data: <?php echo $strratep?>

                }

            ]

        }
        };

   var myLiveChart = new Chart(ctx, chart);
const slider = document.querySelector('.chartAreaWrapper');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', (e) => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener('mouseleave', () => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mouseup', () => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mousemove', (e) => {
  if(!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = (x - startX) * 3; //scroll-fast
  slider.scrollLeft = scrollLeft - walk;
});






} );
</script>