// If Statement

// if ( 3 < 1) {
//     console.log('Link');
// }
// else if ( 2 == 2) {
//     console.log('Gannon');
// }
// else {
//     console.log('Zelda');
// }

// Equal Sign

// =  => value or assignment x = 5
// ==  => comparison ( 2 == "2")
// ===  => must equal ( 2 === 2 )

// Functions

// function add(number1, number2) {
    // let number1 = 5
    // let number2 = 7
    // console.log(number1 + number2);
//     return number1 + number2
// }
// console.log(add(5, 7))
// let result = add(5, 7)
// console.log(result);

// undefined or null

// let x;
// let x = null
// x = 'Coding is fun!'
// console.log(x);

// -----------------------------------------

// Print odds 1-20
// Using a loop write code that will console.log all of the odd values from 1 up to 20

// Print 1-20
// We need a loop
// console.log
// We need values


// for ( i = 0; i <= 20; i++ ) {
//     if ( i % 5 == 0 ) {
//         console.log(i);
//     }
// }

// Sigma
// Write code that will add all of the values from 1-100 onto
// some variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100.
// We should get back 5050 at the end

// Sum 1 - 100 - Done
// variable - Done
// console.log each value - Done
// sum == 5050

// let sum = 0
// // for ( i = 0; i <= 100; i++)
// for ( i = 0; i < 101; i++) {
//     console.log(i + " +");
//     // sum = sum + i
//     sum += i
// }
// console.log(sum);

// let sum = 0
// // for ( i = 0; 1 <= 100; i++)
// for ( i = 0; i < 101; i++) {
//     console.log(i);
//     // sum = sum + i
//     sum += i
// }
// console.log(sum);

// Array Reverse
// Write a function that will reverse the values an array and return them.
// var arr = [ "a", "b", "c", "d", "e"]

// Write a function - Done
// Reverse the Array
// console.log

function reverseArr(arr) {
    for ( i = 0; i < arr.length/2; i++) {
        temp = arr[i]
        arr[i] = arr[arr.length-1-i]
        arr[arr.length-1-i] = temp
    }
    return arr
}
let result = reverseArr([ "a", "b", "c", "d", "e"])
console.log(result);

