""" 
    Advent of Code
    2021 Day 3
    Binary Diagnostic
    
    The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
"""


def import_puzzle(location):
    with open(location, "rt") as f:
       return [entry for entry in f.readlines()]
   
if __name__ == "__main__":
    #diagnostics = import_puzzle("example_input/example_03.txt")
    diagnostics = import_puzzle("puzzle_input/puzzle_03.txt")
    
    width = len(diagnostics[0])-1 #import_puzzle reads a newline for some reason, so -1
    
    gamma_pos = [0 for _ in range(width)]
    epsilon_pos = [0 for _ in range(width)]
    
    for bina in diagnostics:
        for x, j in enumerate(bina):
            if j == '1': gamma_pos[x] +=1
            elif j == '0': epsilon_pos[x] += 1
    
    gamma = ""
    epsilon = ""
    for g, e in zip(gamma_pos, epsilon_pos):
        if g > e: 
            gamma +="1"
            epsilon +="0"
        else: 
            gamma +="0"
            epsilon+="1"
    
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    
    # Part 1 prints 4191876
    print("\nPART 1")
    print(f"Gamma: {gamma}, Epsilon: {epsilon}")
    print(f"Power consumption is: {gamma*epsilon}")
    
    
    # Part 2 - Oxygen generator rating
    # Consider the first bit.
    # Keep only numbers selected by bit criteria. Discard the others. (AND)
    # One number left, stop. Rating value has been found.
    # Else, repeat to the next bit.
    # OGR is the most common value in the current bit position.
    # If 0 and 1 are equal, keep 1.
    # CO2SR is the least common value.
    # If 0 1 and 1 are equal, keep 0.
    
    
    g = diagnostics
    e = diagnostics
    for i in range(width):
        if len(g)>1:
            g_zeroes = len([x for x in g if x[i]=='0'])
            g_ones = len([x for x in g if x[i]=='1'])
            if g_ones >= g_zeroes:
                g = [x for x in g if x[i]=='1']
            else:
                g = [x for x in g if x[i]=='0']

        if len(e)>1:
            e_zeroes = len([x for x in e if x[i]=='0'])
            e_ones = len([x for x in e if x[i]=='1'])
            if e_zeroes >= e_ones:
                e = [x for x in e if x[i]=='0']
            else:
                e = [x for x in e if x[i]=='1']
    
    oxygen,scrubber = int(g[0],2), int(e[0], 2)
    #Part 2 prints 3414905
    print("\nPART 2")
    print(f"OGR: {oxygen}, CO2SR: {scrubber}\nLSR: {oxygen*scrubber}")