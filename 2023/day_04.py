
# This could probably have been made easier using Counter
# but I decided to build my own solution.
# Yesterday I asked for something like Lanternfish, this was it I guess.

class LotteryTicket:
    # Used for part 2
    
    def __init__(self, number, numbers, winning) -> None:
        self.number : int = number
        self.numbers : list[str] = numbers
        self.winning: list[str] = winning
        self.amount = 1

def import_puzzle(path: str):
    
    with open(path, "r", encoding="utf-8") as f:
        puzzle = []
        
        for line in f.readlines():
            puzzle.append(line.strip("\n"))
        
        return puzzle

def solve_part_one(tickets: list[str]):
    
    points = 0
    for ticket in tickets:
        splitted_ticket = ticket.split(":")
        card_no = splitted_ticket[0].split(" ")[1]
        numbers = splitted_ticket[1].split("|")
        winning_numbers = numbers[0].split(" ")
        my_numbers = numbers[1].split(" ")
        while "" in winning_numbers: winning_numbers.remove("")
        while "" in my_numbers: my_numbers.remove("")
        
        power = 0
        
        for number in winning_numbers:
            if number in my_numbers:
                power += 1
                
        if power != 0:
            points += 2 ** (power-1)
    
    print(f"Part one: {points}")

def solve_part_two(tickets: list[str]):
    
    ticket_list: list[LotteryTicket] = []
    
    for ticket in tickets:
        splitted_ticket = ticket.split(":")
        card_no = splitted_ticket[0].split(" ")
        numbers = splitted_ticket[1].split("|")
        winning_numbers = numbers[0].split(" ")
        my_numbers = numbers[1].split(" ")
        
        # Remove whitespace
        while "" in winning_numbers: winning_numbers.remove("")
        while "" in my_numbers: my_numbers.remove("")
        while "" in card_no: card_no.remove("")
        
        # initialize tickets 
        this_ticket = LotteryTicket(int(card_no[1]), my_numbers, winning_numbers)
        ticket_list.append(this_ticket)
    
    # check for winning numbers
    for i, ticket in enumerate(ticket_list):
        additional_tickets = 0
        for number in ticket.winning:
            if number in ticket.numbers:
                additional_tickets += 1
        
        # add new tickets
        for j in range(1, additional_tickets+1):
            try:
                # add new tickets for every ticket
                for _ in range(ticket.amount):
                    ticket_list[i+j].amount += 1
            except IndexError:
                continue
            
    amount_tickets = 0
    for ticket in ticket_list:
        amount_tickets += ticket.amount
    
    print(f"Part two: {amount_tickets}")
        
def main():
    example = import_puzzle("2023/example_input/04.txt")
    solve_part_one(example)
    solve_part_two(example)
    
    puzzle = import_puzzle("2023/puzzle_input/04.txt")
    solve_part_one(puzzle)
    solve_part_two(puzzle)

if __name__ == "__main__":
    main()