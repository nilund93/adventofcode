
def import_puzzle(path: str):
    
    with open(path, "r", encoding="utf-8") as f:
        puzzle = []
        
        for line in f.readlines():
            puzzle.append(line.strip("\n").split(":"))
        
        return puzzle
    
def solve_part_one(puzzle: list[list[str]]):
    
    maximum_colors: dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    sum_of_ids: int = 0
    
    for game in puzzle:
        game_no = game[0].split(" ")[1]
        pulls = game[1].split(";")
        possible = True
        
        for pull in pulls:
            pull = pull.strip(" ")
            colors = pull.split(",")
            
            for color in colors:
                temp = color.lstrip(" ").split(" ")
                if int(temp[0]) > maximum_colors[temp[1]]: possible = False
                
        if possible: sum_of_ids += int(game_no)
    
    print(sum_of_ids)     
    
def solve_part_two(puzzle: list[list[str]]):

    power_of_sets = 0
    
    for game in puzzle:
        possible_colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        pulls = game[1].split(";")
        
        for pull in pulls:
            pull = pull.strip(" ")
            colors = pull.split(",")
            
            for color in colors:
                temp = color.lstrip(" ").split(" ")
                # print(temp)
                if int(temp[0]) > possible_colors[temp[1]]: 
                    possible_colors[temp[1]] = int(temp[0])
        
        power_of_sets += possible_colors["red"]*possible_colors["green"]*possible_colors["blue"]
    
    print(power_of_sets)
    
def main():
    puzzle = import_puzzle("2023/puzzle_input/02.txt")
    example = import_puzzle("2023/example_input/02.txt")
    
    solve_part_one(example)
    solve_part_one(puzzle)
    
    solve_part_two(example)
    solve_part_two(puzzle)
    
if __name__ == "__main__":
    main()
        