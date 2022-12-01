def import_puzzle():
    with open("2022/puzzle_input/01.txt", "rt") as f:
        meals = []
        current_meal = []
        for line in f.readlines():
            
            if line == "\n":
                meal_sum = 0
                for meal in current_meal:
                    meal_sum += meal
                meals.append(meal_sum)
                current_meal.clear()
                
            else:
                line = line.strip("\n")
                current_meal.append(int(line))
        # print(meals)
        return meals
        
def import_example():
    with open("2022/example_input/01.txt", "rt") as f:
        return True
    
def part_one(puzzle):
    """
        Find the elf carrying the most calories.
        How many calories do they carry?
    """
    
    max_calorie = 0
    for meal in puzzle:
        # print(meal)
        if max_calorie < meal:
            max_calorie = meal
    print(f"Maximum calories: {max_calorie}")

def part_two(puzzle):
    """
        How many calories do the top 3 elfs carry?
    """
    print(sum(sorted(puzzle, reverse=True)[0:3]))
    

if __name__ == "__main__":
    
    
    meals = import_puzzle()
    part_one(meals) # prints 69289
    part_two(meals) # prints 205615
    # for meal in meals: print(meal)