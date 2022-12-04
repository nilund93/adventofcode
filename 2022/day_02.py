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
        elif (my_choice == "A" and op_choice == "C"):
            points += 6
        elif (my_choice == "B" and op_choice == "A"):
            points += 6
        elif (my_choice == "C" and op_choice == "B"): 
            points += 6
    print(points)

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
    points = 0
    for round in rounds:
        if round[0]=="A": points +=1
        elif round[0]=="B": points +=2
        elif round[0]=="C": points +=3
        
        if round[1]=="X": pass
        elif round[1]=="Y": points += 3
        elif round[1]=="Z": points += 6
        print(points)
    print(points)

if __name__ == "__main__":
    strategy = import_example()
    # strategy = import_puzzle()
    part_one(strategy) # prints 17189
    part_two(strategy)