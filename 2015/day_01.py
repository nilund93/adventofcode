def import_puzzle():
    with open("2015/puzzle_input/01.txt", "rt") as f:
       return f.readline()

def part_one(puzzle):
    up = puzzle.count("(")
    down = puzzle.count(")") 
    return up-down
   
def part_two(puzzle):
    current_floor = 0
    for i, floor in enumerate(puzzle):
        if floor == "(": current_floor+=1   
        elif floor == ")": current_floor-=1
        
        if current_floor == -1: 
            return (i+1, current_floor)
            
if __name__ == "__main__":
    puzzle = import_puzzle()
    print(f"Part one: {part_one(puzzle)}") #74
    print(f"Part two: {part_two(puzzle)}") #1795