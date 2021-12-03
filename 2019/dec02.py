


    

def intCode(memory, noun, verb):
    pointer = 0
    memory[1] = noun
    memory[2] = verb
    while(True):
        currentOP = memory[pointer]
        if currentOP == 99:
            #print("HALT!")
            return memory[0]

        param_one = memory[pointer+1]
        param_two = memory[pointer+2]
        param_three = memory[pointer+3]

        
        if (currentOP == 1): #Addition intcode
            memory[param_three] = memory[param_one] + memory[param_two]
        elif(currentOP == 2): #Multiplication intcode
            memory[param_three] = memory[param_one] * memory[param_two]
        else:
            print("Something went wrong in intcode")
        pointer += 4
        
    

def bruteForce(memory):
    for noun in range(100):
        for verb in range(100):
            #importFile()
            if(intCode(memory[:], noun, verb) == 19690720):
                return 100*memory[1] + memory[2]


def Main():
    with open("adventofcode/2019/input02.txt", "r") as f:
        memory = [int(intcode) for intcode in f.read().split(",")]
    #importFile()
    intCode(memory[:], 12, 2)
    print("Position 0 is", intCode(memory[:], 12, 2))
    #Part 1: 4576384

    print("The result of 100 * noun + verb-bruteforce is", bruteForce(memory[:]))


Main()