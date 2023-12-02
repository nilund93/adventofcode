# On each line, the calibration value can be found by 
# combining the first digit and the last digit (in that order) 
# to form a single two-digit number.
# What is the sum of all of the calibration values?

def import_puzzle(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def solve(calibrations: list[str]):

    digit_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    
    calibration_sum_one = 0
    
    # Part one
    for line in calibrations:
        # variables
        first: int = None
        last: int = None  
          
        # first numeric
        for symbol in line:
            if symbol.isdigit():
                first = symbol
                break
        
        # last numeric
        for symbol in range(len(line)-1, -1, -1):
            if line[symbol].isdigit():
                last = line[symbol]
                break
            
        calibration_sum_one += int(first + last)
    
    # Part two
    calibration_sum_two = 0
    
    for line in calibrations:
        # variables
        first = None
        last = None
        
        # first digit
        for i in range(len(line)):
            if line[i].isdigit():
                first = line[i]
                break
            
            for word in digit_words:
                if line[i:].startswith(word):
                    first = digit_words[word]
                    break
                
            if first: break
        
        # last digit
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                last = line[i]
                break
            
            for word in digit_words:
                if line[i:].startswith(word):
                    last = digit_words[word]
                    break
                
            if last: break
        
        calibration_sum_two += int(first + last)
                    
    return calibration_sum_one, calibration_sum_two
    
    
def main():
    example = import_puzzle("2023/example_input/01.txt")
    puzzle = import_puzzle("2023/puzzle_input/01.txt")
    
    print(solve(example))
    print(solve(puzzle))

if __name__ == "__main__":
    main()

