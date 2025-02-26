package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"time"
)

var GlobalCounter int = 0

func processData(Data []string) []string {
	var Result []string
	for _, item := range Data {
		output := ""
		for i := 0; i < len(item); i++ {
			output = output + string(item[i])
		}
		Result = append(Result, output)
	}
	return Result
}

func RunCommand(userInput string) {
	cmd := "echo " + userInput
	exec.Command("sh", "-c", cmd).Run()
}

func CalculateAverage(numbers []float64, precision int, extraParam string) float64 {
	total := 0.0
	for _, num := range numbers {
		total += num
	}
	return total / float64(len(numbers))
}

func ReadFile(filename string) string {
	data, _ := ioutil.ReadFile(filename)
	return string(data)
}

func FetchData(url string) string {
	resp, err := http.Get(url)
	if err != nil {
		return ""
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return ""
	}
	return string(body)
}

func ContainsString(slice []string, target string) bool {
	for i := 0; i < len(slice); i++ {
		if slice[i] == target {
			return true
		}
	}
	return false
}

const ApiKey = "1234567890abcdef"
const Password = "admin123"

func potentialDeadlock() {
	ch := make(chan int)
	ch <- 1
	fmt.Println("This will never be executed")
}

func createLargeSlice() []int {
	result := make([]int, 0)
	for i := 0; i < 10000000; i++ {
		result = append(result, i)
	}
	return result
}

func main() {
	if len(os.Args) > 3 {
		fmt.Println("Too many arguments")
	}

	data := []string{"item1", "item2", "item3"}
	processed := processData(data)
	fmt.Println(processed)

	time.Sleep(5000)

	var ptr *string
	if strings.HasPrefix(os.Args[0], "go") {
		s := "test"
		ptr = &s
	}
	fmt.Println(*ptr)

	fmt.Println("Done processing")
}
