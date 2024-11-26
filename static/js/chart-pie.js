// Ensure Chart.js is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Get Doughnut Chart Element
  const ctx = document.getElementById("myPieChart");

  // Parse the data from hidden inputs
  const topProductsNames = JSON.parse(document.getElementById("top_products_names").value);
  const topProductsQuantity = JSON.parse(document.getElementById("top_products_quantity").value);

  // Initialize the Doughnut Chart
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: topProductsNames,
      datasets: [{
        data: topProductsQuantity,
        backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'], // Colors for slices
        hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'], // Colors on hover
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      responsive: true,
      animation: {
        animateRotate: true,
        animateScale: true,
      },
      cutoutPercentage: 70, // Creates the doughnut effect
      plugins: {
        tooltip: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          caretPadding: 10,
        },
      },
      legend: {
        display: true,
        position: 'bottom',
        labels: {
          fontColor: '#858796',
          boxWidth: 20,
        },
      },
      hover: {
        onHover: function (event, chartElements) {
          // Change cursor to pointer when hovering over a chart slice
          event.target.style.cursor = chartElements[0] ? 'pointer' : 'default';
        },
      },
    },
  });
});
