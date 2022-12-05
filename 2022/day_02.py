def import_puzzle():
    with open("2022/puzzle_input/02.txt", "rt") as f:
        return [line.strip("\n").split(" ") for line in f.readlines()]
        
def import_example():
    with open("2022/example_input/02.txt", "rt") as f:
        return [line.strip("\n").split(" ") for line in f.readlines()]

def part_one(rounds):
    """
        A Rock
        B Paper
        C Scissors
        
        X Rock
        Y Paper
        Z Scissors
        
        Rock 1 point
        Paper 2 points
        Scissors 3 points
        Draw 3 points
        Win 6 points
    """
    points = 0
    for round in rounds:
        op_choice = round[0]
        my_choice = round[1]
        if my_choice == "X": my_choice = "A"
        elif my_choice == "Y": my_choice = "B"
        elif my_choice == "Z": my_choice = "C"
        if my_choice == "A": points +=1
        elif my_choice == "B": points +=2
        elif my_choice == "C": points +=3
        
        
        if my_choice == op_choice: points +=3
        elif (my_choice == "A" and op_choice == "C") or \
             (my_choice == "B" and op_choice == "A") or \
             (my_choice == "C" and op_choice == "B"): 
                points += 6
    print(f"Part 1: {points}")

def part_two(rounds):
    
    """ 
        Opponent
        A Rock
        B Paper
        C Scissors
        
        X Lose
        Y Draw
        Z Win

        Rock 1 point
        Paper 2 points
        Scissors 3 points
        Draw 3 points
        Win 6 points
    """
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}
    loss = {"A": "Z", "B": "X", "C": "Y"}
    shape_points = {"X": 1, "Y": 2, "Z": 3}
    points = 0
    
    for round in rounds:
        op_choice = round[0]
        outcome = round[1]
        
        my_choice = ""
        if outcome == "X":      # loss
            my_choice = loss[op_choice]
        elif outcome == "Z":    # win
            my_choice = wins[op_choice]
            points += 6
        else:                   # draw
            my_choice = draws[op_choice]
            points += 3
        points += shape_points[my_choice]            
    print(f"Part 2: {points}")

if __name__ == "__main__":
    # strategy = import_example()
    strategy = import_puzzle()
    part_one(strategy) # prints 17189
    part_two(strategy) # prints 13490