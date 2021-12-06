"""
    Advent of Code
    2021 Day 6
    Lanternfish
    
    The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

    A massive school of glowing lanternfish swims past. 
    They must spawn quickly to reach such large numbers - maybe exponentially quickly? 
    You should model their growth rate to be sure.
    
    TODO: Make population_count work for example-input 
          It currently takes for granted that all ages are included, which example does not include.
    
"""
from collections import Counter

def import_puzzle(location):
    with open(location, "rt") as f:
        return [int(entry) for entry in f.readline().split(",")]

def population_array(fishes, p2):
    # this is the 3head solution - p2 will never finish
    fish_timers = []
    
    for fish in fishes:
        fish_timers.append(fish)
    
    # loop for 80 or 256 days
    days = 256 if p2 else 80
    
    for day in range(days):
        # go through every fish and remove one day, if the timer has reached -1, spawn a new fish with timer 6
        new_fish = []
        for fish in enumerate(fish_timers):
            fish_timers[fish[0]] -= 1
            if fish_timers[fish[0]] == -1:
                new_fish.append(8)
                fish_timers[fish[0]] = 6
                
        fish_timers.extend(new_fish)
    return len(fish_timers)

def population_count(fishes, p2):
    fish_counter = Counter(fishes)
    days = 256 if p2 else 80
    
    # loop for 256 or 80 days
    for _ in range(1, days+1):
        new_and_old_fishes = fish_counter[0]
        
        # go through every day
        for i in range(8):
            fish_counter[i] = fish_counter[i+1]
        fish_counter[8] = new_and_old_fishes
        fish_counter[6] += new_and_old_fishes
        
    # return all entries of fishes, giving us the total population
    # please stop multiplying
    return sum(fish_counter.values())
        


if __name__ == "__main__":
    
    example = import_puzzle("adventofcode/2021/example_input/example_06.txt")
    puzzle = import_puzzle("adventofcode/2021/puzzle_input/puzzle_06.txt")
    
    part_one = population_array(puzzle, False)
    #part_one = population_array(example, False)
    print(f"Part 1: {part_one} lanternfishes")
    
    part_two = population_count(puzzle, True)
    #part_two = population_count(example, True)
    print(f"Part 2: {part_two} lanternfishes")
    
    
    