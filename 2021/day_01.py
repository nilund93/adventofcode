# Advent of Code Day 1 2021
# Sonar Sweep

# We're getting a list of depth measurements from our sonar device.
# We need to calculate how many times our measurements are larger than the previous one.

# Merry Christmas!

def import_puzzle():
    with open("puzzle_input/puzzle_01.txt", "rt") as f:
       return [int(entry) for entry in f.readlines()]

def calculate_increases(data):
    inc = 0
    for m in range(1, len(data)):
        if data[m] > data[m-1]: inc+=1
        
    return inc

if __name__ == "__main__":
    measurements = import_puzzle()
    increases = calculate_increases(measurements)
    print(f"Part one: {increases}") # Part one prints 1342
    
    # part two
    triplets = []
    for i in range(len(measurements)-2):
        # create a list of sums
        triplets.append(sum([measurements[i], measurements[i+1], measurements[i+2]]))
    
    part_two = calculate_increases(triplets)
    print(f"Part two: {part_two}") # Part two prints 1378
        