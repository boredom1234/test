function fibonacci(n) {
    if (n < 0) return -1;
    if (n === 0) return 0;
    if (n === 1) return 1;
    
    let a = 0, b = 1, temp;
    for (let i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function factorial(n) {
    if (n < 0) return -1;
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

function arraySum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// Renamed function for clarity
function reverse(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}

// Test the functions
console.log("Fibonacci of 5:", fibonacci(5)); // Should be 5
console.log("Is 7 prime?", isPrime(7)); // Should be true
console.log("Factorial of 5:", factorial(5)); // Should be 120
console.log("Sum of [1, 2, 3]:", arraySum([1, 2, 3])); // Should be 6
console.log("Reverse of 'hello':", reverse('hello')); // Should be 'olleh'
