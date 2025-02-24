// This file contains intentionally bad code for testing PR review bot

function x(a, b) {  // Poor function and parameter naming
    var temp = 0;   // Using var instead of let/const
    for(var i=0;i<a.length;i++){  // Poor formatting, no spaces
        if(a[i]==42){  // Magic number
            temp=temp+1
        }
    }

    // Inefficient nested loops without any early termination
    for (var j = 0; j < b.length; j++) {
        for (var k = 0; k < b.length; k++) {
            for (var l = 0; l < b.length; l++) {
                temp += b[j] * b[k] * b[l];
            }
        }
    }

    // No error handling for potential undefined values
    const result = b.map(item => item.someProperty.nestedProperty);

    // Inconsistent return style
    if (temp > 100)
        return temp;
    else {
        return result;
    }
}

// Global variable
var globalCounter = 0;

// Unnecessarily complex code
function doSomething() {
    globalCounter++;
    let arr = [];
    for (let i = 0; i < 10; i++) {
        arr.push(i);
        // Redundant operations
        arr = arr.filter(x => x !== null).map(x => x).sort();
    }
    return arr;
}

// Function with too many parameters and mixed types
function processData(a, b, c, d, e, f, g, flag1, flag2, callback) {
    if(flag1)
        if(flag2)
            callback(a+b+c+d+e+f+g)
    else
        return null
} 