
def import_puzzle(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return_list = []
        for line in f.readlines():
            return_list.append(line.strip("\n"))
        
        return return_list

def solve_part_one(schematic: list[str]):
    # What is the sum of all part numbers in the engine
    # schematic? (All parts adjacent to a symbol are correct.)
    
    width: int = len(schematic[0])
    height: int = len(schematic)
    schematic_sum: int = 0
    
    for i, line in enumerate(schematic):
        # i is line number, line is the line
        for j, column in enumerate(line):
            
            # check if a special symbol is found
            if column != "." and not column.isdigit():
                
                # check upper left of the symbol
                if schematic[i-1][j-1].isdigit(): 
                    schematic_sum += int(schematic[i-1][j-1])
                    
                
                
                
                # [i-1][j-1]
                # [i-1][j]
                # [i-1][j+1]
                # [i][j-1]
                # [i][j+1]
                # [i+1][j-1]
                # [i+1][j]
                # [i+1][j+1]
    
    print(schematic_sum)    

def main():
    example = import_puzzle("2023/example_input/03.txt")
    solve_part_one(example)

if __name__ == "__main__":
    main()