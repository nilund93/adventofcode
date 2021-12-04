"""
    Advent of Code
    2021 Day 4
    Giant Squis
    
    You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. 
    What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
    Maybe it wants to play bingo?
    Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
    Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. 
    (Numbers may not appear on all boards.) 
    If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
    
"""

def import_puzzle(location):
    with open(location, "rt") as f:
        return [card for card in f.read().split("\n\n")]
    
def add_drawn(card, draw):
    return [['*' if i == draw else i for i in line] for line in card]

def check_win(card):
    # first statement checks for full lines
    # second statement checks for full column by looking at that index in every row
    return (any(all(i == '*' for i in line) for line in card) or
            any(all(line[idy] == '*' for line in card) for idy in range(len(card[0]))))

def get_score(card, draw):
    # score of the winning board is calculated by finding the sum of all the unmarked numbers on the board
    # multiply that sum by the last number that was called
    
    cardsum = 0
    for line in card:
        linesum = 0
        for number in line:
            if number != '*':
                linesum += number
        cardsum += linesum
    return cardsum*draw

if __name__ == "__main__":
    #cards = import_puzzle("2021/example_input/example_04.txt")
    cards = import_puzzle("2021/puzzle_input/puzzle_04.txt")
    # first line is the drawn numbers
    drawn = [int(i) for i in cards.pop(0).split(",")]
    # the rest are the cards
    player_cards = [[[int(i) for i in line.split()] for line in card.split('\n')] for card in cards]


    win = False
    for draw in drawn:
        player_cards = [add_drawn(card, draw) for card in player_cards]
        
        for card in player_cards:
            if(check_win(card)) and not win:
                score = get_score(card, draw)
                print(f"Part 1: {score}\n")
                win = True
            elif len(player_cards) == 1:
                score = get_score(player_cards[0], draw)
                print(f"Part 2: {score}")
        player_cards = [card for card in player_cards if not check_win(card)]
        

    

"""
    Took a bunch of inspiration from /u/zedrdave on reddit for this solution.
    Learned a bunch.
    Going to redo it at a later date to see if I can figure it out more by myself.
    
    Things learned:
     - list comprehension
     - next()-function - I didnt use it but I learned about it
     - how close I am to a brain aneurysm 
"""