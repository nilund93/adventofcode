"""
    Advent of Code 2020 Day 6
    --- Day 6: Custom Customs ---
    I didn't sign up for doing surveys
    
"""

def main():
    with open("Hobbyprojekt/adventofcode/2020/inputdec06.txt", "r") as f:
        puzzle_input = [line for line in f.readlines()]
    
    with open("Hobbyprojekt/adventofcode/2020/example06.txt", "r") as g:
        example_input = [line for line in g.readlines()]

    #inp = example_input
    inp = puzzle_input

    #list() will be used because [] does not convert tupples to items
    groups = [list()]
    index = 0
    for line in inp:
        if line == "\n":
            groups.append(list())
            index+=1
        else:
            groups[index].append(list(line[:-1]))

    """
        #We want to calculate all the questions that SOMEONE answered yes to
    """
    total_yes = 0
    total_agreed_answers = 0
    for group in groups:
        every_answer = []
        for answers in group:
            every_answer.extend(answers)
        total_yes+=len(set(every_answer)) #We care only IF someone answered, thus set
        
        #part 2, count the questions where EVERYONE in the group answered yes
        common_answer = every_answer.copy()
        for answers in group:
            common_answer = set(answers).intersection(common_answer)
        total_agreed_answers += len(common_answer)
    
    print(total_yes, total_agreed_answers)
    #Part 1 prints 6249
    #Part 2 prints 3103

    """
        Comment:
        I had a hard time figuring out the difference between [] and list()
        This code also doesn't work unless the inputfile has a \n as it's last row
        Without it, the last group of answers won't be counted
    """
    
    

main()