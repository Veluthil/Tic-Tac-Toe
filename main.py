from art import logo, winner_x, winner_o, draw


def create_board():
    grid = f" {board_positions[0]} | {board_positions[1]} | {board_positions[2]} \n" \
           f"-----------\n" \
           f" {board_positions[3]} | {board_positions[4]} | {board_positions[5]} \n" \
           f"-----------\n" \
           f" {board_positions[6]} | {board_positions[7]} | {board_positions[8]} "
    return grid


board_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

list_of_x = []
list_of_o = []

player_x = True
winner = False
board = create_board()

print(logo)
print("Welcome to the Tic Tac Toe game!\n\n"
      "The board looks like that:\n")
print(create_board())
print("\nPlayer ❌ uses ❌s and Player ⭕ uses ⭕s.\n"
      "Player ❌ begins!\n")

while not winner:
    if len(list_of_x) == 5:
        print(draw)
        print("That's a draw!")
        break
    elif player_x:
        try:
            position = int(input("Write a number where you want to put your ❌: "))
            if position in list_of_o or position in list_of_x:
                print(f"Your opponent or you have already chosen place {position}, try again.")
            elif position not in board_positions:
                print("Your number does not exist on board, try again and choose number 0-8.")
            else:
                list_of_x.append(position)
                board = board.replace(str(board_positions[position]), "❌")
                print(board)
                for combo in winning_combinations:
                    if set(combo).issubset(list_of_x) and len(set(list_of_x)) >= 3:
                        print(winner_x)
                        print("Player ❌ is a winner!")
                        winner = True
                    else:
                        player_x = False
        except ValueError:
            print("You must choose a number between 0 and 8.")

    else:
        try:
            position = int(input("Write a number where you want to put your ⭕: "))
            if position in list_of_o or position in list_of_x:
                print(f"Your opponent or you have already chosen place {position}, try again.")
            elif position not in board_positions:
                print("Your number does not exist on board, try again and choose number 0-8.")
            else:
                list_of_o.append(position)
                board = board.replace(str(board_positions[position]), "⭕")
                print(board)
                for combo in winning_combinations:
                    if set(combo).issubset(list_of_o) and len(set(list_of_o)) >= 3:
                        print(winner_o)
                        print("Player ⭕ is a winner!")
                        winner = True
                    else:
                        player_x = True
        except ValueError:
            print("You must choose a number between 0 and 8.")
