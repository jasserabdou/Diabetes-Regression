document.addEventListener("DOMContentLoaded", function () {
  var prediction = "{{ prediction }}";

  console.log(prediction);

  var predictionResult = prediction;

  var predictionElement = document.getElementById("prediction");

  predictionElement.textContent = predictionResult;
});
