let checklistTitle =
  document.querySelector(".popup-container").dataset.checklist;
// const previousBtn = document.querySelector("#previousBtn");
// const nextBtn = document.querySelector("#nextBtn");
const checklists = [
  "Morning Routine",
  "Evening Skincare Routine",
  "Weekly Self-Care",
  "Daily Gratitude",
];
const filePath = "test.xlsx";

function toggle() {
  const toggles = document.querySelectorAll(".toggle-container");

  toggles.forEach(function (toggle) {
    const circle = toggle.querySelector(".circle");

    toggle.addEventListener("click", function () {
      let state = toggle.dataset.state;
      let text = toggle.parentNode.querySelector("p");

      if (state === "off") {
        toggle.style.backgroundColor = "#e654a5";
        toggle.style.justifyContent = "flex-end";
        circle.style.transform = "translateX(1%)";
        toggle.dataset.state = "on";
        text.style.textDecoration = "line-through";
      } else if (state === "on") {
        toggle.style.justifyContent = "flex-start";
        toggle.style.backgroundColor = "#91e8e8";
        circle.style.transform = "translateX(0)";
        toggle.dataset.state = "off";
        text.style.textDecoration = "none";
      }
    });
  });
}

// --------------------------------- //

function createListItems(data, title) {
  const ul = document.querySelector(".list-container ul");
  let h1 = document.querySelector("h1");
  h1.textContent = title;

  for (const item of data) {
    const li = document.createElement("li");
    const theText = item["List Item"];

    const html = `<p>${theText}</p><span class="toggle-container" data-state="off"><div class="circle"></div></span>`;
    li.innerHTML = html;
    ul.appendChild(li);
  }

  toggle();
}

// --------------------------------- //

fetch(filePath)
  .then((response) => response.arrayBuffer())
  .then((data) => {
    const workbook = XLSX.read(data, { type: "array" });
    const worksheet = workbook.Sheets[workbook.SheetNames[0]];
    const jsonData = XLSX.utils.sheet_to_json(worksheet);

    const correctChecklist = jsonData.filter(
      (row) => row["Type of Checklist"] === checklistTitle
    );

    createListItems(correctChecklist, checklistTitle);
  })
  .catch((error) => console.error(error));
