package main

import "fmt"

// Define a function that explicitly takes a slice of integers
func sumNumbersInSlice(numbers []int) int {
	total := 0
	for _, num := range numbers {
		total += num // The compiler knows 'num' will always be an int
	}
	return total
}

func main() {
	// Scenario 1: Correct usage
	mySlice := []int{1, 2, 3}
	fmt.Printf("Sum of mySlice: %d\n", sumNumbersInSlice(mySlice))

	// Scenario 2: Incorrect usage - Go prevents this at compile time
	// This line would cause a compile-time error:
	// cannot use [1 2 "three" 4] (type []interface {}) as type []int in argument to sumNumbersInSlice
	// numbersWithString := []interface{}{1, 2, "three", 4} // This would be the "Pythonic" equivalent of mixed types
	// fmt.Printf("Sum of numbersWithString: %d\n", sumNumbersInSlice(numbersWithString))

	// To even try to make this work, you'd have to use type assertion or other mechanisms,
	// which forces you to explicitly handle the potential type mismatch.
}

// func sumNumbersInSlice(numbers []int) int: -> Notice the type declaration []int for the numbers parameter.
// This tells the Go compiler that sumNumbersInSlice expects a slice where every element is an integer.
