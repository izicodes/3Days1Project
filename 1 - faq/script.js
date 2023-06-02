// 1 - Select all of the question bars on the page
let questionBars = document.querySelectorAll(".question-bar");

// 2 - create a forEach loop for each question
questionBars.forEach(function (questionBar) {
  // 3 - Create an event listener for each question when clicked
  questionBar.addEventListener("click", function () {
    // 4 - Create the variables for the question and the answer
    let questionNumber = this.getAttribute("data-question");
      let answer = document.querySelector(`p[data-answer="${questionNumber}"]`);
      let icon = questionBar.querySelector("i");

    // 5 - if statement if the answer has the .hide class set already or not
    if (answer.classList.contains("hide")) {
      // 6.1 - if it does have the .hide class set, remove it
        answer.classList.remove("hide");
        icon.classList.remove("fa-plus");
        icon.classList.add("fa-minus");
    } else {
      // 6.2 - if it doesn't have the .hide class set (you can see the answer), add it
        answer.classList.add("hide");
        icon.classList.add("fa-plus");
        icon.classList.remove("fa-minus");
    }
  });
});
