def import_puzzle():
    with open("2015/puzzle_input/02.txt", "rt") as f:
        boxes = []
        for line in f.readlines():
            
            measures = line.rstrip("\n")
            measures = measures.split("x")
            boxes.append(measures)
        return boxes
    #    return [map(int, i.split("x")) for i in f.readlines()]

def part_one(puzzle: list(list())):
    
    #length, width, height
    total_area = 0
    for box in puzzle:
        length = int(box[0])
        width = int(box[1])
        height = int(box[2])
        # print(length, width, height)
        one_side = 2*length*width
        other_side = 2*width*height
        third_side = 2*height*length
        # print(one_side, other_side, third_side)
        smallest = min(one_side, other_side, third_side)
        right_rect_prism = one_side + other_side + third_side
        paper = smallest/2 + right_rect_prism
        total_area += paper
        # print(right_rect_prism, smallest)
    return int(total_area)
        
def part_two(puzzle: list(list())):
    pass    
    
 
if __name__ == "__main__":
    puzzle = import_puzzle()
    example = [['2', '3', '4']]
    print(part_one(example))
    print(part_one(puzzle)) # 1598415