package main

import (
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readInput() {
	filePath := os.Arg[1]
	windowSize, err := strconv.Atoi(os.Args[2])
	check(err)
	data, err := strings.split(string(data), "\n")
	return 1
}

func PartOne() {

}

func main() {
	puzzleInput = readInput()

	fmt.println(part_one)
}
