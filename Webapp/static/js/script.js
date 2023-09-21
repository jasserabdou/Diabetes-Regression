document.addEventListener("DOMContentLoaded", function () {
  var rangeInputs = document.querySelectorAll('input[type="range"]');
  rangeInputs.forEach(function (input) {
    var output = document.getElementById(
      "output" + input.id.charAt(0).toUpperCase() + input.id.slice(1)
    );
    output.textContent = input.value;

    input.addEventListener("input", function () {
      output.textContent = this.value;
    });
  });
});
