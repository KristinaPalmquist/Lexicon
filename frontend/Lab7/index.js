// // 1. Rectangle
// console.group("1. Rectangle");
// class Rectangle {
//   constructor(width, height, color) {
//     this.width = width;
//     this.height = height;
//     this.color = color;
//   }
//   calcArea() {
//     return this.width * this.height;
//   }
// }
// let rect = new Rectangle(4, 5, "red");
// console.log(rect.width);
// console.log(rect.height);
// console.log(rect.color);
// console.log(rect.calcArea());
// console.groupEnd();
// console.log("");

// // 2. Person
// console.group("2. Person");
class Person {
  constructor(firstName, lastName, age, email) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.email = email;
  }
  toString() {
    return `${this.firstName} ${this.lastName} (age: ${this.age} email: ${this.email})`;
  }
}
// let person = new Person(
//   "Maria",
//   "Petterson",
//   22,
//   "mp@gmail.com"
// );
// console.log(person.toString());
// console.groupEnd();
// console.log("");

// 3. Get Persons
console.group("3. Get Persons");
function getPersons() {
  let person1 = new Person(
    "Maria",
    "Petterson",
    22,
    "mp@gmail.com"
  );
  let person2 = new Person("Lexicon");
  let person3 = new Person("Stefan", "Larsson", 25);
  let person4 = new Person(
    "Peter",
    "Jansson",
    24,
    "ptr@live.com"
  );
  return [person1, person2, person3, person4];
}
console.table(getPersons());
console.groupEnd();
console.log("");

// // 4. Circle
// console.group(`4. Circle`);
// class Circle {
//   constructor(radius) {
//     this.radius = radius;
//   }
//   get diameter() {
//     return this.radius * 2;
//   }
//   set diameter(value) {
//     this.radius = value / 2;
//   }
//   area() {
//     return (
//       Math.round(
//         Math.PI * this.radius * this.radius * 100
//       ) / 100
//     );
//   }
// }
// let c = new Circle(2);
// console.log(`Radius: ${c.radius}`);
// console.log(`Diameter: ${c.diameter}`);
// console.log(`Area: ${c.area()}`);
// console.log("");
// c.diameter = 1.6;
// console.log(`Radius: ${c.radius}`);
// console.log(`Diameter: ${c.diameter}`);
// console.log(`Area: ${c.area()}`);
// console.groupEnd();
// console.log("");

// // 5. Point Distance
// console.group(`5. Group Distance`);
// class Point {
//   constructor(x, y) {
//     this.x = x;
//     this.y = y;
//   }
//   static distance(pointA, pointB) {
//     let distX = pointA.x - pointB.x;
//     let distY = pointA.y - pointB.y;
//     let distance = Math.sqrt(distX * distX + distY * distY);
//     return distance;
//   }
// }
// let p1 = new Point(5, 5);
// let p2 = new Point(9, 8);
// console.log(Point.distance(p1, p2));
// console.groupEnd();
