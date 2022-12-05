def import_puzzle():
    with open("2022/puzzle_input/04.txt", "rt") as f:
        return [line.strip("\n").split(",") for line in f.readlines()]
        
def import_example():
    with open("2022/example_input/04.txt", "rt") as f:
        return [line.strip("\n").split(",") for line in f.readlines()]
    
def part_one(pairs : list()):
    total: int = 0
    for pair in pairs:
        elf_one_min, elf_one_max, elf_two_min, elf_two_max = \
            int(pair[0].split("-")[0]),\
            int(pair[0].split("-")[1]),\
            int(pair[1].split("-")[0]),\
            int(pair[1].split("-")[1])
        if ((elf_one_min <= elf_two_min) and (elf_one_max >= elf_two_max)) or \
            ((elf_two_min <= elf_one_min) and (elf_two_max >= elf_one_max)):
            total +=1
    print(f"Part one: {total}")

def part_two(pairs : list()):
    total: int = 0
    
    for pair in pairs:
        elf_one = list(map(int, pair[0].split("-")))
        elf_two = list(map(int, pair[1].split("-")))
        for i in range(elf_one[0], elf_one[1]+1):
            if i in range(elf_two[0], elf_two[1]+1):
                total += 1
                break
    print(f"Part two: {total}")

if __name__ == "__main__":
   pairs = import_puzzle()
#    pairs = import_example() 
   part_one(pairs) # prints 530
   part_two(pairs) # prints 903