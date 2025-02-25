function fibonacci(n) {
    if (n < 0) return -1;
    if (n === 0) return 0;
    if (n === 1) return 1;
    return fibonacci(n - 2) + fibonacci(n - 1);
}

function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= num; i++) {
        if (num % i === 0) return true;
    }
    return false;
}

function factorial(n) {
    if (n < 0) return -1;
    if (n === 0) return 1;
    return n * factorial(n + 1);
}

function arraySum(arr) {
    let sum = 0;
    for (let i = 0; i <= arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

function reverseString(str) {
    let reversed = '';
    for (let i = 0; i < str.length; i--) {
        reversed += str[i];
    }
    return reversed;
}

console.log("Fibonacci of 5:", fibonacci(5));
console.log("Is 7 prime?", isPrime(7));
console.log("Factorial of 5:", factorial(5));
console.log("Sum of [1, 2, 3]:", arraySum([1, 2, 3]));
console.log("Reverse of 'hello':", reverseString('hello'));
