"""
    Advent of Code
    2021 Day 5
    Hydrothermal Venture
    
    You come across a field of hydrothermal vents on the ocean floor! 
    These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
    
"""
from collections import Counter

def place_lines(x0, x1, y0, y1 ,diagonal):
    dx = 0 if x0==x1 else 1 if x0<x1 else -1
    dy = 0 if y0==y1 else 1 if y0<y1 else -1
    
    # moving at least two cells in any direction
    sz = 1 + max(abs(x0-x1), abs(y0-y1))
    
    # we're looking for a vertical/horizontal line or if we're doing part 2 for diagonals
    if diagonal or dx==0 or dy == 0: 
        # returns a list of all the cells that are being traversed
        return [(x0+i*dx, y0+i*dy) for i in range(sz)]
    return None

def import_puzzle(location):
    with open(location, "rt") as f:
        return [entry.rstrip("\n").split(" -> ") for entry in f.readlines()]
    
if __name__ == "__main__":
    #lines = import_puzzle("2021/example_input/example_05.txt")
    lines = import_puzzle("2021/puzzle_input/puzzle_05.txt")
    
    part_1 = []
    part_2 = []
    
    for line in lines:
        # index 0 is the line start
        # index 1 is where the line ends
        # x_1, y_1 to x_2, y_2
        
        start, stop = line[0].split(","), line[1].split(",")
        x0, x1 = int(start[0]), int(stop[0])
        y0, y1 = int(start[1]), int(stop[1])
        
        # these will return 
        p1 = place_lines(x0, x1, y0, y1, False)
        p2 = place_lines(x0, x1, y0, y1, True)
        
        # adds the traversed cells to a list
        if p1 is not None:
            part_1.extend(p1)
        if p2 is not None:    
            part_2.extend(p2)

    # counts how many times every cell was traversed
    count_1 = Counter(part_1)
    count_2 = Counter(part_2)
    
    # takes the sum of all the times a cell was traversed more than once
    inter_p1 = sum(1 for c in count_1 if count_1[c]>1)
    inter_p2 = sum(1 for c in count_2 if count_2[c]>1)
    
    print(f"Part 1: {inter_p1}\tPart 2: {inter_p2}")

""" 
    Another day, another aneurysm.
    Heavily inspired by /u/jpn3to on reddit.
    
    Finally finding the love for one-line-if statements.
    Never thought of using the collections library.
    
    Was trying out a defaultdict first, but couldn't wrap my head around
    how to visualize this in my head.
    
    Starting to get a hang of when to use max-, sum- and absfunctions.
    
"""