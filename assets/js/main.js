console.log("ACADEMY OMEN IS COOL");

// get element by id message
const message = document.getElementById("message");
const button = document.getElementById("submitBtn");
const file = document.getElementById("file");

// if button is clicked, check the file input
button.addEventListener("click", function (event) {
  if (file.files.length === 0) {
    message.innerHTML = "No File selected, Please select a file!";
  } else {
    message.innerHTML = "Processing Image....";
  }
});
