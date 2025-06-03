let header1 = document.querySelector("h1");
let header2 = document.querySelector("h2");
// header.style.color = "red";
// header.innerText = "HEEEJ";

function getRandomColor() {
  let letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function changeHeaderColor() {
  color1 = getRandomColor();
  console.log(color1);
  color2 = getRandomColor();
  console.log(color2);
  header1.style = `background: linear-gradient(to top, ${color1},  ${color2});
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;`;
  header2.style = `background: linear-gradient(to top, ${color1},  ${color2});
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;`;
}

setInterval(changeHeaderColor, 500);
