def import_puzzle():
    with open("2022/puzzle_input/06.txt", "rt") as f:
        return f.readline()
        
def import_example():
    with open("2022/example_input/06.txt", "rt") as f:
        return f.readlines()
    
def part_one(datastream):
    # markern är fyra lång
    marker = 0
    for i in range(4, len(datastream)):
        if len(set(datastream[i-4:i])) == 4:
            marker = i
            break
    print(f"Part one: {marker}")

def part_two(datastream):
    marker = 0
    for i in range(14, len(datastream)):
        if len(set(datastream[i-14:i])) == 14:
            marker = i
            break
    print(f"Part two: {marker}")
    
if __name__ == "__main__":
    datastream_example = import_example()
    print("Example")
    for line in datastream_example:
        part_one(line.strip("\n"))
    
    print("Actual")
    datastream = import_puzzle()
    part_one(datastream) # prints 1655
    part_two(datastream) # prints 2665