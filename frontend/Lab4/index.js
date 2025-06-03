// // PROBLEM 1:
// console.group("PROBLEM 1 - SLEEPING IN:");
// function sleepIn(weekday, vacation) {
//   return !weekday || vacation;
// }
// console.log(sleepIn(false, false));
// console.log(sleepIn(true, false));
// console.log(sleepIn(false, true));
// console.groupEnd();

// // PROBLEM 2:
// console.group("PROBLEM 2 - MONKEY TROUBLE:");
// function monkeyTrouble(aSmile, bSmile) {
//   return aSmile == bSmile;
// }
// console.log(monkeyTrouble(true, true));
// console.log(monkeyTrouble(false, false));
// console.log(monkeyTrouble(true, false));
// console.groupEnd();

// // PROBLEM 3:
// console.group("PROBLEM 3 - STRING TIMES:");
// function stringTimes(str, n) {
//   return str.repeat(n);
// }
// console.log(stringTimes("Hi", 2));
// console.log(stringTimes("Hi", 3));
// console.log(stringTimes("Hi", 1));
// console.groupEnd();

// PROBLEM 4:
console.group("PROBLEM 4 - LUCKY SUM:");
function luckySum(a, b, c) {
  if (a == 13) {
    return 0;
  } else if (b == 13) {
    return a;
  } else if (c == 13) {
    return a + b;
  } else {
    return a + b + c;
  }
}
console.log(luckySum(1, 2, 3));
console.log(luckySum(1, 2, 13));
console.log(luckySum(1, 13, 3));
console.groupEnd();

// PROBLEM 5:
console.group("PROBLEM 5 - CAUGHT SPEEDING:");
function caughtSpeeding(speed, birthday) {
  let limit = 60;
  if (birthday) {
    limit += 5;
  }
  if (speed > limit + 20) {
    return 2;
  } else if (speed > limit) {
    return 1;
  } else {
    return 0;
  }
}
console.log(caughtSpeeding(60, false));
console.log(caughtSpeeding(65, false));
console.log(caughtSpeeding(65, true));
console.groupEnd();
