# Advent of Code Day 2 2021
# Dive!

# We're getting a list of instructions for our submarine to follow.
# We need to calculate how the product of our depth and horizon.

# Merry Christmas!

def import_puzzle(location):
    with open(location, "rt") as f:
       return [entry.split() for entry in f.readlines()]

if __name__ == "__main__":
    
    # input is a list where pos 0 is direction, pos 1 is how far
    instructions = import_puzzle("puzzle_input/puzzle_02.txt")
    #instructions = import_puzzle("example_input/example_02.txt")
    
    # part 1
    horizon = 0
    depth = 0
    
    # forward X increases the horizontal position by X units.
    # down X increases the depth by X units.
    # up X decreases the depth by X units.
    
    for movement in instructions:
        if movement[0] == 'forward': horizon += int(movement[1])
        elif movement[0] == 'down': depth -= int(movement[1])
        elif movement[0] == 'up': depth += int(movement[1])
    
    #print(horizon, depth)
    print(f"{horizon * abs(depth)}") # part 1 prints 1746616
    
    #part 2
    aim = 0
    depth = 0
    horizon = 0
    
    # down X increases your aim by X units.
    # up X decreases your aim by X units.
    # forward X does two things:
    #     It increases your horizontal position by X units.
    #     It increases your depth by your aim multiplied by X.
    
    for movement in instructions:
        if movement[0] == 'forward': 
            horizon += int(movement[1])
            depth += aim * int(movement[1])
        elif movement[0] == 'down': aim -= int(movement[1])
        elif movement[0] == 'up': aim += int(movement[1])
    
    #print(f"{horizon}, {depth}, {aim}")
    print(f"{horizon * abs(depth)}")
    
            