"""
    Advent of Code 2018
    Day 1

    We need to calibrate the frequency.
    Input is a bunch of instructions for the calibration.
    Output should be the final frequency
"""
def part_one(puzzle_input):
    frequency = 0
    for line in puzzle_input:
        if(line[0] == "+"):
            frequency += int(line[1:])
        elif(line[0] == "-"):
            frequency -= int(line[1:])

    print("PART ONE".center(20))
    print("Frequency should be set to", frequency) #486

def part_two(puzzle_input):
    freq_set = set()
    frequency = 0
    print("PART TWO".center(20))
    statement = True
    while statement:
        for line in puzzle_input:
            if(line[0] == "+"): frequency += int(line[1:])
            elif(line[0] == "-"):   frequency -= int(line[1:])
            
            if(frequency in freq_set):
                print("Frequency found! It is", frequency)
                statement = False
                break
            else: 
                freq_set.add(frequency) #69285
            
        

with open("2018/puzzle_input/01.txt", "r") as f:
        puzzle_input = [line for line in f.readlines()]
f.close()
print("\n\n\n\n")
part_one(puzzle_input)
print("\n\n")
part_two(puzzle_input)




