
def import_puzzle(path: str):
    
    with open(path, "r", encoding="utf-8") as f:
        return f.readline().split()[1:], f.readline().split()[1:]
    
def solve_part_one(times: list(), distances: list()):
    win_races = []
    
    for time, dist in zip(times, distances):
        amount = 0
        for i, j in zip(range(0, int(time)), range(int(time), 0, -1)):
            if i*j > int(dist): amount += 1
        win_races.append(amount)
    answer = 1
    for num in win_races:
        answer *= num
    
    print(answer)
    
def solve_part_two(times: list(), distances: list()):
    time = ''.join(times)
    distance = ''.join(distances)
    amount = 0
    for i, j in zip(range(0, int(time)), range(int(time), 0, -1)):
            if i*j > int(distance): amount += 1
    
    print(amount)

def main():
    example_times, example_dist = import_puzzle("2023/example_input/06.txt")
    solve_part_one(example_times, example_dist)
    solve_part_two(example_times, example_dist)
    print("-------------------------")
    
    puzzle_times, puzzle_dist = import_puzzle("2023/puzzle_input/06.txt")
    solve_part_one(puzzle_times, puzzle_dist)
    solve_part_two(puzzle_times, puzzle_dist)

if __name__ == "__main__":
    main()
