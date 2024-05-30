import time

class Player:
    def __init__(self, player_number, player_surname, player_first_name, player_height, player_weight, player_year_of_birth):
        self.number = player_number
        self.surname = player_surname
        self.first_name = player_first_name
        self.height = player_height
        self.weight = player_weight
        self.won = 0
        self.tie = 0
        self.points = 0
        self.year_of_birth = player_year_of_birth
        self.fights = 0

    def __ge__(self, player_two):
        return self.height >= player_two.height and self.weight >= player_two.weight

    def __str__(self):
        return (f"{self.first_name} {self.surname}, {self.year_of_birth}, "
                f"{self.height}cm, {self.weight}kg, fights participated in {self.fights} combat games: "
                f"{self.won} x won, {self.tie} x tie = {self.points} points")

    def game_results(self, final_result):
        if final_result == 'won':
            self.points += 10
            self.won += 1
        elif final_result == 'tie':
            self.points += 5
            self.tie += 1
        self.fights += 1

def get_valid_input(prompt, type_func):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_func.__name__}.")

def create_player(players):
    while True:
        number = get_valid_input("Input number: ", int)
        if any(player.number == number for player in players):
            print("That player number already exists in the records! try a different one")
        else:
            break
    surname = input("Input surname: ")
    first_name = input("Enter the player's first name: ")
    height = get_valid_input("Input the player's height in cm: ", int)
    weight = get_valid_input("Input the player's weight in kg: ", float)
    year_of_birth = get_valid_input("Enter the year of birth: ", int)
    return Player(number, surname, first_name, height, weight, year_of_birth)

def manage_game(players):
    number1 = get_valid_input("Input the number of the first player: ", int)
    number2 = get_valid_input("Input the number of the second player: ", int)

    player1 = next((p for p in players if p.number == number1), None)
    player2 = next((p for p in players if p.number == number2), None)

    if not player1 or not player2:
        print("One of the players does not exist.")
        return

    if player1.fights >= 3 or player2.fights >= 3:
        print("One player has reached the participation limit of 3")
        return

    result = input("Input the result for the first player, type either (won/tie/lost): ").strip().lower()

    if result == 'won':
        player1.game_results('won')
        player2.game_results('lost')
    elif result == 'tie':
        player1.game_results('tie')
        player2.game_results('tie')
    elif result == 'lost':
        player1.game_results('lost')
        player2.game_results('won')
    else:
        print("Invalid result entered.")
        return

    if player1 >= player2:
        height_diff = player1.height - player2.height
        weight_diff = player1.weight - player2.weight
        print(f"Player {player1.first_name} {player1.surname} has won, "
              f"he is {abs(height_diff)} cm {'taller' if height_diff > 0 else 'shorter'} and "
              f"{abs(weight_diff)} kg {'heavier' if weight_diff > 0 else 'lighter'} than player {player2.first_name} {player2.surname}")
    else:
        height_diff = player2.height - player1.height
        weight_diff = player2.weight - player1.weight
        print(f"Player {player2.first_name} {player2.surname} has won, "
              f"he is {abs(height_diff)} cm {'taller' if height_diff > 0 else 'shorter'} and "
              f"{abs(weight_diff)} kg {'heavier' if weight_diff > 0 else 'lighter'} than player {player1.first_name} {player1.surname}")

def list_players(players):
    print("Fetching Players Data...")
    time.sleep(1)
    for player in players:
        print(player)

def main():
    players = []
    while True:
        print("\nMenu:")
        print("1. Create A New Player")
        print("2. Manage Game")
        print("3. List Players")
        print("4. Output Winner")
        print("5. Exit Program")
        choice = input("Type a number to select an option from the menu: ").strip()

        if choice == '1':
            if len(players) >= 6:
                print("Cannot add more than 6 players.")
            else:
                player = create_player(players)
                players.append(player)
                print("A new player has been created successfully.")
        elif choice == '2':
            if players:
                manage_game(players)
            else:
                print("No players available. Create players first.")
        elif choice == '3':
            if players:
                list_players(players)
            else:
                print("No players available.")
        elif choice == '4':
            if players:
                winner = max(players, key=lambda p: p.points)
                print(f"Current winner is {winner}")
            else:
                print("No players available.")
        elif choice == '5':
            break
        else:
            print("Your choice is invalid.")

if __name__ == "__main__":
    main()
