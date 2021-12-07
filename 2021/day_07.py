"""
    Advent of Code
    2021 Day 7
    The Treachery of Whales
    
    A giant whale has decided your submarine is its next meal, and it's much faster than you are. 
    There's nowhere to run!

    Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) 
    zooms in to rescue you! 
    They seem to be preparing to blast a hole in the ocean floor; 
    sensors indicate a massive underground cave system just beyond where they're aiming!
    
"""
from statistics import median

def import_puzzle(location):
    with open(location, "rt") as f:
        return sorted([int(entry) for entry in f.readline().split(",")])

def mean_crab(crabs):
    return sum(crabs)//len(crabs)

def gauss(element):
    return element * (element + 1) // 2
    

if __name__ == "__main__":
    crabs = import_puzzle("2021/puzzle_input/puzzle_07.txt")
    example = import_puzzle("2021/example_input/example_07.txt")
    
    # part 1 - we need to sort a list and use the distance from the median as fuel consumption
    # input is already sorted from import_puzzle
    med = round(median(crabs))
    cost_p1 = 0
    for crab_pos in crabs:
        cost_p1 += abs(med - crab_pos)
    print(f"{cost_p1} fuel.") # Part 1 prints 335330
    
    # part 2 - we need to calculate the gauss formula using the absolute value of the mean value and the crabs position
    
    mean = mean_crab(crabs)
    cost_p2 = 0
    for crab in crabs:
        cost_p2 += gauss((abs(crab - mean)))
        
    print(f"Part 2: {cost_p2} fuel.") # Part 2 prints 92439766
    
        
    