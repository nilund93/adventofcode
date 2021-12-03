# Count IDs that have exactly two of any letter
# also
# Count IDs that with exactly three of any letter
# Multiply the two IDs

def read_puzzle(path):
    """Reads a file from variable path and returns a list from
    containg puzzle inputs

    Args:
        path (filepath): [path of puzzle.txt]

    Returns:
        [list]: [puzzle converted to list]
    """
    f = open(path, "rt")
    puzzle_list = [entry for entry in f.readlines()]
    f.close()
    return puzzle_list

def check_Doubles(boxes):
    doubles = 0
    for box in boxes:
        letter_set = set(box)
        for letter in letter_set:
            if box.count(letter) == 2: 
                doubles +=1
                break
            
    return doubles
    

def check_Tripples(boxes):
    triples = 0
    
    for box in boxes:
        letter_set = set(box)            
        for letter in letter_set:
            if box.count(letter) == 3: 
                triples +=1
                break
            
    return triples

def get_difference(boxes):
    for box in boxes:
        box_set_one = set(box)
        len_box = len(box_set_one)
        for box_2 in boxes:
            box_set_two = set(box_2)
            len_box_two = len(box_set_two)
            box_dif = box_set_one.intersection(box_set_two)
            if(len_box - 1 == len(box_dif) and len_box_two -1 == len(box_dif)):
                for letter in box_dif:
                    print(letter, end="")
            

def main():
    example = read_puzzle("example_input/02.txt")
    puzzle = read_puzzle("puzzle_input/02.txt")
    
    print(f"Doubles: {check_Doubles(example)}\tTripples: {check_Tripples(example)}\tChecksum: {check_Doubles(example) * check_Tripples(example)}")
    print(f"Doubles: {check_Doubles(puzzle)}\tTripples: {check_Tripples(puzzle)}\tChecksum: {check_Doubles(puzzle) * check_Tripples(puzzle)}")

    get_difference(read_puzzle("example_input/02_p2.txt"))
    get_difference(puzzle)
if __name__ == "__main__":
    main()