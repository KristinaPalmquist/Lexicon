// 1. Show sum
function calc() {
  let num1 = Number(document.getElementById("num1").value);
  console.log(num1);
  let num2 = Number(document.getElementById("num2").value);
  console.log(num2);
  document.getElementById("sum").value = num1 + num2;
}

// 2. Show more
function showText() {
  let textEl = document.getElementById("text");
  let moreEl = document.getElementById("more");
  if (textEl.style.display == "none") {
    textEl.style.display = "block";
    moreEl.innerText = "Show less";
  } else {
    textEl.style.display = "none";
    moreEl.innerText = "Read More...";
  }
}

// 3. Collect List Item
function extractText() {
  let liText = document.querySelectorAll("li");
  let textBox = document.getElementById("result");
  textBox.value = "";
  for (let text of liText) {
    textBox.value += text.innerText + "\n";
  }
}

// 4. Add and Delete
function addItem() {
  let list = document.getElementById("items4");
  let newTextValue =
    document.getElementById("newText").value;

  newTextValue =
    newTextValue.charAt(0).toUpperCase() +
    newTextValue.slice(1);

  let listItem = document.createElement("li");
  listItem.textContent = newTextValue + " - ";

  let linkItem = document.createElement("a");
  linkItem.href = "#";
  linkItem.textContent = "Delete";
  linkItem.onclick = function (e) {
    e.preventDefault();
    deleteItem(listItem);
  };

  listItem.appendChild(linkItem);
  list.appendChild(listItem);
  document.getElementById("newText").value = "";

  function deleteItem(listItem) {
    list.removeChild(listItem);
  }
}

// 5. Stopwatch
function stopwatch() {
  let startBtn = document.getElementById("startBtn");
  let stopBtn = document.getElementById("stopBtn");
  let timeEl = document.getElementById("time");

  let minutes = 0;
  let seconds = 0;
  let timeValue = "";

  let timer;

  startBtn.onclick = function (e) {
    e.preventDefault();
    timer = setInterval(updateTime, 1000);
    startBtn.disabled = true;
    stopBtn.disabled = false;
  };

  stopBtn.onclick = function (e) {
    e.preventDefault();
    clearInterval(timer);
    stopBtn.disabled = true;
    startBtn.disabled = false;
  };

  function updateTime() {
    seconds++;
    if (seconds == 60) {
      minutes++;
      seconds = 0;
    }
    if (minutes < 10 && seconds < 10) {
      timeValue = "0" + minutes + ":0" + seconds;
    } else if (seconds < 10) {
      timeValue = minutes + ":0" + seconds;
    } else if (minutes < 10) {
      timeValue = "0" + minutes + ":" + seconds;
    } else {
      timeValue = minutes + ":" + seconds;
    }
    timeEl.innerText = timeValue;
  }
}
