"""
    Advent of Code
    2021 Day 8
    Seven Segment Search
    
    You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. 
    Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

    As your submarine slowly makes its way through the cave system, 
    you notice that the four-digit seven-segment displays in your submarine are malfunctioning; 
    they must have been damaged during the escape. 
    You'll be in a lot of trouble without them, so you'd better figure out what's wrong.
    
"""
def import_puzzle(location):
    with open(location, "rt") as f:
        return [entry.rstrip("\n").split("|") for entry in f.readlines()]
    

if __name__ == "__main__":
    example = import_puzzle("2021/example_input/example_08.txt")
    puzzle = import_puzzle("2021/puzzle_input/puzzle_08.txt")
    
    for line in example:
        pattern = line[0]
        output = line[1]
        print(pattern, output)