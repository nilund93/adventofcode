"""
    Advent of Code 2020 Day 3
    ..# Toboggan Trajectory #..
    It's downhill from here...
    
"""
def countTrees(slopes, right, down):
    trees = 0
    iterations=0
    row = 0

    #step through the slopes with the "speed" as step length
    for i in range(0,len(slopes),down):

        """
        ...due to something you read about once involving arboreal genetics and
        biome stability, the same pattern repeats to the right many times.
        """
        relative_row = row % len(slopes[i])

        """
            Trees look weird in this place.
        """
        if(slopes[i][relative_row] is "#"): 
            trees+=1
        row+=right
    return trees

def arborealStop(tries, slopes):
    trees = 1
    for i in tries:
        trees*=countTrees(slopes, i[0], i[1])
    return trees

def main():
    with open("adventofcode/2020/inputdec03.txt", "r") as f:
        puzzle_input = [line.strip() for line in f.readlines()]
    
    example_input = ["..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]
    
    
    print("Trees encountered", countTrees(example_input, 3, 1))
    print("Trees encountered", countTrees(puzzle_input, 3, 1))
    #part 1: 289 trees
    #Store the try-pairs in a list for part 2
    tries=[[1,1], [3,1], [5,1], [7,1], [1,2]]
    print("Product of the trees: ", arborealStop(tries, example_input))
    print("Product of the trees: ", arborealStop(tries, puzzle_input))
    #part 2: 5522401584

main()