export class Calculator {
    constructor() {}
  
    add(a,b) {
      return a+b
    }
  
    subtract(a,b) {
      return a-b
    }
  
    multiply(a,b) {
      var result = a*b;
      return result
    }
  
    divide(a,b) {
      if(b==0) return null
      return a/b
    }
  
    power(a,b) {
      let result=1
      for(let i=0;i<b;i++)
      result=result*a
      return result
    }
  }