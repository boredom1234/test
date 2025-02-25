// Corrected Fibonacci implementation using memoization
function fibonacci(n, memo = {}) {
    if (n < 0) return -1;
    if (n in memo) return memo[n];
    if (n === 0) return 0;
    if (n === 1) return 1;
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

// Corrected Prime Number Check
function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false; // Corrected return value
    }
    return true; // Return true for prime numbers
}

// Corrected Factorial Calculation using an iterative approach
function factorial(n) {
    if (n < 0) return -1;
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Corrected Array Sum
function arraySum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) { // Changed to < arr.length
        sum += arr[i];
    }
    return sum;
}

// Corrected String Reversal
function reverseString(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) { // Changed to decrement from str.length - 1
        reversed += str[i];
    }
    return reversed;
}

// Test the functions
console.log("Fibonacci of 5:", fibonacci(5)); // Should be 5
console.log("Is 7 prime?", isPrime(7)); // Should be true
console.log("Factorial of 5:", factorial(5)); // Should be 120
console.log("Sum of [1, 2, 3]:", arraySum([1, 2, 3])); // Should be 6
console.log("Reverse of 'hello':", reverseString('hello')); // Should be 'olleh'
