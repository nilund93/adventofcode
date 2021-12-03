"""
    Advent of Code 2020 Day 5
    --- Day 5: Binary Boarding ---
        Boarding planes sucks.
                >:(
    
"""
import collections  #Needed for set

def calculateSeat(seat):
    """
        Replace letters with binary.
        Convert string to integer with base 2
        Return the integer
    """
    seatnumber = 0
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")
    seatnumber = int(seat, 2)  
    return seatnumber

def main():
    with open("Hobbyprojekt/adventofcode/2020/inputdec05.txt", "r") as f:
        puzzle_input = [l for l in f.read().split("\n")]
    
    example_input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

    """
        F means front
        B means back
        L means left
        R means right
        128 rows
        labeled 0 to 127
        0 to 63: Front
        64 to 127 Back

        We need to find row, column and seat ID
        Seat ID is calculated by: row*8 + col

        It is also a binary number. :)
    """

    for i in example_input:
        print("Example input ID", i, "is", calculateSeat(i))

    print("Puzzle input")
    highest_seat = 0
    seats = set() #required for part 2
    
    for j in puzzle_input:
        check = calculateSeat(j)
        seats.add(check)
        highest_seat = max(check, highest_seat)
    print("Highest seat ID is:", highest_seat)
    #Highest seat is: 828
    
    for i in range(256*8):
        if(i not in seats) and (i+1 in seats) and (i-1 in seats):
            print("My seat is:", i)
    #My seat is: 565

main()
