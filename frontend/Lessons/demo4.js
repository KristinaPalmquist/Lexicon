// document.getElementById("demo1").innerText =
//   "JavaScript is cool";
// console.log("lokijuh");
// // let age = prompt("how old are you?");
// // document.getElementById("demo2").innerText += age;

// console.log("2" == 2);
// console.log("2" === 2);

// var x = 1;
// var y = 2;

// q1 = "2" == y && x === 1;
// // true && true => true

// q2 = x >= 0 || y === "2";
// // true || false => true

// q3 = !(x !== 1) && y === 1 + 1;
// // !false && true => true

// q4 = y !== x || y == "2" || x === 3;
// // true || true || false => true
// console.log(q1);
// console.log(q2);
// console.log(q3);
// console.log(q4);

// var x = 0;
// var y = 10;

// WHILE
// while (x < 5) {
//   console.log("x is currently " + x);
//   console.log("y is currently " + y);
//   if (x === 3) {
//     console.log("x is " + x);
//     break;
//   }
//   x++;
//   y--;
// }

// FOR

// for (i = 0; i < 10; i++) {
//   console.log(i);
// }

// var word = "ABCDEFGHIJK";
// for (i = 0; i < word.length; i++) {
//   console.log(i + ": " + word[i]);
// }

// let word = "ABABABABABABABABABA";
// for (i = 0; i < word.length; i = i + 2) {
//   console.log(word[i]);
// }

// FUNCTIONS
// function hello() {
//   console.log("Hello");
// }
// hello();

let helloYou = function (name) {
  console.log("hello " + name);
};

helloYou("name");

function addNum(num1, num2) {
  console.log(num1 + num2);
}

addNum(30, "20");

// function helloSomeone(name = "Aladdin") {
//   console.log("Hello " + name);
// }

// /*
// In Python:
// def hello_someone(name='Aladdin'):
//   print('Hello', name)
//  */
// helloSomeone();
// helloSomeone("Bob");
