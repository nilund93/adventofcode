

def importFile():
    f = open("adventofcode/2019/input01.txt", "r")
    masses = [int(module_mass) for module_mass in f.readlines()]
    return masses
def calculate_fuel(mass):
    current_mass = mass//3 -2
    #return current_mass # for problem 1
    #return-statement for problem 2
    if current_mass <= 0: return 0
    return current_mass + calculate_fuel(current_mass) 

def Main():
    #import and tokenize file
    masses = importFile()
    totalfuel = 0
    #first problem
    for mass in masses:
        totalfuel += calculate_fuel(mass)
    print(totalfuel)
    #first problem prints 3353880
    #second problem prints 5027950
    

Main()