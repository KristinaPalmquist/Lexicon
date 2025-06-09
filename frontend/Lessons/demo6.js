console.log("demo6");

// var header = document.querySelector("h1");

// // header.style.color = "red";

// function getRandomColor() {
//   var letters = "0123456789ABCDEF";
//   var color = "#";
//   for (var i = 0; i < 6; i++) {
//     color += letters[Math.floor(Math.random() * 16)];
//   }
//   return color; //#F1A2B3
// }

// function changeHeaderColor() {
//   colorInput = getRandomColor();
//   header.style.color = colorInput;
// }

// setInterval("changeHeaderColor()", 500);

// // Synchronous code (sync)
// console.log("start");
// for (let i = 1; i <= 3; i++) {
//   console.log(i);
// }
// console.log("end");

// // Asynchronous code (async)
// console.log("start");
// setTimeout(function () {
//   console.log("first");
// }, 2000);
// setTimeout(function () {
//   console.log("second");
// }, 3000);
// setTimeout(function () {
//   console.log("third");
// }, 1000); // 1 second
// console.log("end");

// // Promises
// console.log("Start");
// const delay = (ms) =>
//   new Promise((resolve) => setTimeout(resolve, ms));
// delay(1000)
//   .then(() => {
//     console.log("Inside promise");
//   })
//   .then(() => {
//     console.log("End promise");
//   });
// console.log("End of code");

// // Arrow functions
// var add1 = function (x, y) {
//   return x + y;
// };
// const add2 = (x, y) => x + y;
// console.log(add1(8, 9));
// console.log(add2(2, 3));

// // Traditional function
// function Person1() {
//   this.age = 0;
//   setInterval(function growUp() {
//     this.age++; // 'this' does NOT refer to the Person object (leading to error)
//   }, 1000);
// }
// // Arrow function
// function Person2() {
//   this.age = 0;
//   setInterval(() => {
//     this.age++; // 'this' properly refers to the Person object (no error)
//   }, 1000);
// }

// console.log("Traditional Function: ");
// const array = [1, 2, 3, 4];
// const squares = array.map(function (x) {
//   return x * x;
// });
// console.log(squares);
// console.log("Arrow Function: ");
// const squaresArrow = array.map((x) => x * x);
// console.log(squaresArrow);

// // Objects
// class User {
//   constructor(firstName, lastName, email) {
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.email = email;
//     this.loggedIn = false;
//   }
//   login() {
//     this.loggedIn = true;
//     console.log(`${this.firstName} has logged in`);
//   }
//   logout() {
//     if (this.loggedIn) {
//       this.loggedIn = false;
//       console.log(`${this.firstName} has logged out`);
//     } else {
//       console.log(`${this.firstName} is NOT logged in`);
//     }
//   }
// }

// let userOne = new User(
//   "Kristina",
//   "Palmquist",
//   "example@email.se"
// );

// let userTwo = new User(
//   "Aladdin",
//   "Lexicon",
//   "email@lexicon.se"
// );

// userTwo.login();
// userOne.login();
// userTwo.logout();

// // GETTERS and SETTERS
// class Person{
//     constructor(firstName, lastName){
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }
//     get fullName(){
//         return `${this.firstName} ${this.lastName}`;
//     }
//     set fullName(value){
//         const parts = value.split(' ');
//         this.firstName = parts[0];
//         this.lastName = parts[1];
//         console.warn('Changed the name')
//     }
// }

// const p1 = new Person('John', 'Doe');

// console.log(p1.fullName);
// p1.fullName = "Bob Bobson";
// console.log(p1.fullName);


class UserService {
  constructor(uri) {
    this.baseUri = uri; // uniform resource identifier
  }

  static signUp(user) {
    console.log(`Registering user`);
    console.log(user);
  }
  static signIn(email, password) {
    console.log(
      `Logging in user with ${email} and password is: ${password}`
    );
  }
}

UserService.signUp({
  firstName: "John",
  lastName: "Smith",
});
UserService.signIn("john@smith.com", "pocahontas123");
