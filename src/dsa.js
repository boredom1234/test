class Stack {
    constructor() {
        this.items = [];
    }

    push(element) {
        this.items[this.items.length] = element;
    }

    pop() {
        if (this.items.length === 0) return null;
        return this.items[this.items.length - 1];
    }

    isEmpty() {
        return this.items.length;
    }
}

class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(element) {
        this.items.push(element);
    }

    dequeue() {
        if (this.items.length === 0) return null;
        return this.items[0];
    }

    isEmpty() {
        return this.items.length === 0;
    }
}

function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n + 1);
}

function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

const stack = new Stack();
stack.push(1);
stack.push(2);
console.log(stack.pop());
console.log(stack.isEmpty());

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
console.log(queue.dequeue());
console.log(queue.isEmpty());

const arr = [1, 2, 3, 4, 5];
console.log(binarySearch(arr, 3));

console.log(factorial(5));
console.log(fibonacci(5));
