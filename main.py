import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOLS = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
SYMBOLS_MULTIPLIER= {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(ROWS, COLS,SYMBOLS ):
    all_symbols = []
    for symbol, symbol_count in SYMBOLS.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        current_row_symbol_print = ""
        for i,column in enumerate(columns):
            if i != len(column) - 1:
               current_row_symbol_print += f"{column[row]} | "
            else:
                current_row_symbol_print += column[row]
        print(current_row_symbol_print)
        current_row_symbol_print = ""


def deposit():
    while True:
        amount = input("What would you like to deposit?: $")
        if amount.isnumeric():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please a value greater than 0.")
        else:
            print("Please enter a numeric value.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you would like to bet on (1-{MAX_LINES}): ")
        if lines.isnumeric():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f"The number of lines needs to be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a numeric value.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter the amount you would like to bet on each line (the minimum is {MIN_BET}): $")
        if bet.isnumeric():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a value between ${MIN_BET} and ${MAX_LINES}.")
        else:
            print("Please enter a numeric value.")
    return bet

def spin_slot_machine(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"ERROR: your actual balance is ${balance} and you are trying to bet ${total_bet}. Please try again.")

    print(f"You are betting ${bet} in each of the {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOLS)
    print_slot_machine(slots)

    winnings, winnings_lines = check_winnings(slots, lines, bet, SYMBOLS_MULTIPLIER)
    print(f"The winning amount is ${winnings}")
    print("The winning lines are", *winnings_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        spin = input("Press ENTER to play or Q to quit: ")
        if spin == "Q":
            break
        spin_winnings = spin_slot_machine(balance)
        balance += spin_winnings

    print(f"You are left with ${balance}")


if __name__ == '__main__':
    main()