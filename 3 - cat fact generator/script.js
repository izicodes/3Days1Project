// Variables
const catFact = document.querySelector(".cat-fact");
const generateBtn = document.querySelector("button");
const nekoImage = document.querySelector(".img-container img");

// Run the function to begin with
getFact();

// Function that fetches the fact via the API
function getFact() {
  fetch("https://catfact.ninja/fact")
    .then((response) => response.json())
    .then((data) => {
      // Handle the response data
      var fact = data["fact"];
      catFact.textContent = fact;
    })
    .catch((error) => {
      // Handle any errors
      console.error("Hello: " + error);
    });
}

// When you click the button, a new fact appears + new Neko image
generateBtn.addEventListener("click", function () {
  getFact();

  const imageNum = Math.floor(Math.random() * 7);
  nekoImage.setAttribute("src", "images/" + imageNum + ".jpg");
});
