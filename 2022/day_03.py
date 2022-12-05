values = {"a": 1, "b": 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v":22, "w": 23, "x": 24,
          "y":25, "z": 26, "A": 27, "B": 28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
          "K":37, "L":38, "M":39, "N":40, "O": 41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U": 47, "V":48,
          "W":49, "X":50, "Y":51, "Z":52}


def import_puzzle():
    with open("2022/puzzle_input/03.txt", "rt") as f:
        return [line.strip("\n") for line in f.readlines()]
        
def import_example():
    with open("2022/example_input/03.txt", "rt") as f:
        return [line.strip("\n") for line in f.readlines()]
    
def part_one(rucksacks : list()):
    unique_letters = []
    
    for rucksack in rucksacks:
        item_one = set(rucksack[0:len(rucksack)//2])
        item_two = set(rucksack[len(rucksack)//2:])
        unique_item = item_one.intersection(item_two)
        if len(unique_item) > 0:
            unique_letters.append(unique_item.pop())
    
    unique_values = []
    
    for letter in unique_letters:
        unique_values.append(values[letter])
    
    print(f"Part one: {sum(unique_values)}")
    
def part_two(rucksacks : list()):
    
    badge_letters = []
    for i in range(0, len(rucksacks), 3):
        elf_one = set(rucksacks[i])
        elf_two = set(rucksacks[i+1])
        elf_three = set(rucksacks[i+2])
        
        badge = elf_one.intersection(elf_two).intersection(elf_three)

        if len(badge) > 0:
            badge_letters.append(badge.pop())
    
    badge_values = []
    for letter in badge_letters:
        badge_values.append(values[letter])
    
    print(f"Part two: {sum(badge_values)}")
    
if __name__ == "__main__":
    # rucksacks = import_example()
    rucksacks = import_puzzle()
    part_one(rucksacks) # prints 7674
    part_two(rucksacks) # prints 2805