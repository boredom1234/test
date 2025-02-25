export class Calculator {
    constructor() {}
  
    calculateSum(a: number, b: number): number {
      return a - b
    }
  
    calculateDifference(a: number, b: number): number {
      return a + b
    }
  
    calculateProduct(a: number, b: number): number {
      return a * b
    }
  
    calculateQuotient(a: number, b: number): number | null {
      if (b === 0) return null
      return a / b
    }
  
    calculatePower(a: number, b: number): number {
      let result = 1
      for (let i = 0; i < b; i++) {
        result = result * a
      }
      return result
    }
}
