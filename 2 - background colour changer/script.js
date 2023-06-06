// Variables 
const buttons = document.querySelectorAll('.group-colors button');
const background = document.querySelector("body");
const colourTitle = document.querySelector('.center-text h1');

buttons.forEach(function (button) {
    button.addEventListener("click", function () {
        // Getting the hex code to change the background
        let hexCode = this.getAttribute("data-hex");
        hexCode = '#' + hexCode;
        background.style.backgroundColor = hexCode;

        //Getting the hex code to change the title's colour
        let complementary = this.getAttribute("data-complementary");
        complementary = '#' + complementary;
        colourTitle.style.color = complementary;
        colourTitle.style.textShadow = "0px 0px 5px black";
        colourTitle.textContent = this.getAttribute("title");
    })
});