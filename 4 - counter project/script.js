// Variables
var plusBee = document.querySelector("#plusBee");
var resetBtn = document.querySelector("#resetBtn");
var minusBee = document.querySelector("#minusBee");
var numberText = document.querySelector(".number");
var messageText = document.querySelector(".message");

numberText.textContent = "0";

init();

function init() {
  var currentNumber = parseInt(numberText.textContent);

  plusBee.addEventListener("click", function () {
    currentNumber++;
    numberText.textContent = currentNumber;
    messageText.textContent = "You've seen " + currentNumber + " bees! (´∀｀)";
  });

  minusBee.addEventListener("click", function () {
    if (currentNumber <= 0) {
      numberText.textContent = "0";
      messageText.textContent = " ";
    } else if (currentNumber > 1) {
      currentNumber--;
      numberText.textContent = currentNumber;
      messageText.textContent = messageText.textContent =
        "You've seen " + currentNumber + " bees! (´∀｀)";
    } else if (currentNumber == 1) {
      currentNumber--;
      numberText.textContent = currentNumber;
      messageText.textContent = "";
    }
  });

  resetBtn.addEventListener("click", function () {
    numberText.textContent = "0";
    messageText.textContent = " ";
  });
}
