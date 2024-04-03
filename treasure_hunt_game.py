"""
This is a program that allows the user to play a mini Treasure Hunt Game
This will be done on a grid where the user will enter coordinates to move around the grid.
The mechanics are similar to Minesweeper in the sense that some grid spaces will give
them points whereas others will reduce their points
"""


import random


def get_grid_size() -> list[int] | None:
    """Function that allows the player to choose what size grid they want to play they game on"""
    choosing_grid_size = True

    while choosing_grid_size:
        change_grid_size = input("""The default grid size is 8x8.
Would you like to change it?
Enter yes or no.
""").lower()
        if change_grid_size == "no":
            return [8, 8]
        if change_grid_size == "yes":
            grid_size_option = input(
                """You can choose the following grid sizes:
(1) 6x6
(2) 10x10
(3) 12x12
(4) Cancel and continue with default settings.
Enter the number of the choice you would like to use
""")
            if grid_size_option == "1":
                return [6, 6]
            if grid_size_option == "2":
                return [10, 10]
            if grid_size_option == "3":
                return [12, 12]
            if grid_size_option == "4":
                return [8, 8]
            print("You have entered an invalid number")
        else:
            print("You need to enter 'yes' or 'no'.")
    return None


def get_chest_amount() -> int | None:
    """Function that allows the user to choose the number of chests they play with"""
    choosing_chests = True

    while choosing_chests:
        change_number_of_chests = input("""The default number of chests is 5.
Would you like to change it?
Enter yes or no.
""").lower()
        if change_number_of_chests == "no":
            return 5
        if change_number_of_chests == "yes":
            number_of_chests_option = input("""You can choose the following amount of chests:
(1) 10
(2) 15
(3) Cancel and continue with default settings.
Enter the number of the choice you would like to use
""")
            if number_of_chests_option == "1":
                return 10
            if number_of_chests_option == "2":
                return 15
            if number_of_chests_option == "3":
                return 5
            print("You have entered an invalid number.")
        else:
            print("You need to enter 'yes' or 'no'.")
    return None


def get_bandit_amount() -> int | None:
    """Function that allows the user to choose the number of bandits they play against"""
    choosing_bandits = True

    while choosing_bandits:
        change_number_of_bandits = input("""The default number of bandits is 5.
Would you like to change it?
Enter yes or no.
""").lower()
        if change_number_of_bandits == "no":
            return 5
        if change_number_of_bandits == "yes":
            number_of_bandits_option = input("""You can choose the following amount of bandits:
(1) 10
(2) 15
(3) Cancel and continue with default settings.
Enter the number of the choice you would like to use
""")
            if number_of_bandits_option == "1":
                return 10
            if number_of_bandits_option == "2":
                return 15
            if number_of_bandits_option == "3":
                return 5
            print("You have entered an invalid number.")
        else:
            print("You need to enter 'yes' or 'no'.")
    return None


def create_grid(grid_dimensions: list[int]) -> list[str]:
    """Function that creates the grid of the game"""
    grid = [[" " for x in range(grid_dimensions[0])]
            for y in range(grid_dimensions[1])]
    return grid


def set_chests_and_bandits(grid: list[str], grid_occupier: str, grid_dimensions: list[int],
                           player_pos: list[int]) -> list[str] | None:
    """
    Function that sets a chests or a bandit on the grid randomly.
    grid_occupier is the string label for either a chest or bandit.
    This function will only set the chest or bandit on a suitable space that isn't already occupied
    """
    finding_suitable_space = True

    while finding_suitable_space:
        x = random.randint(0, grid_dimensions[0]-1)
        y = random.randint(0, grid_dimensions[1]-1)
        if (x != player_pos[0] or y != player_pos[1]) and (grid[y][x] == " "):
            grid[y][x] = grid_occupier
            return grid
    return None


def populate_grid(grid: list[str], chest_count: int, bandit_count: int, grid_dimensions: list[int],
                  player_pos: list[int]):
    """
    This function will populate the grid with bandits and chests
    Chests are set as 0 to represent 0 visits because this game has a mechanic where 
    if you visit a chest 3 times, the chest is removed from the board and replaced by a bandit.
    This stops the player from finding one chest and automatically winning by
    continuously visiting the same chest until they reach the gold threshold.
    """
    for _ in range(0, chest_count):
        grid = set_chests_and_bandits(
            grid, "0", grid_dimensions, player_pos)

    for _ in range(0, bandit_count):
        grid = set_chests_and_bandits(
            grid, "B", grid_dimensions, player_pos)

    return grid


def show_grid(grid_dimensions: list[int], player_pos: list[int]):
    """Function that displays the grid to the user"""
    for y in range(0, grid_dimensions[1]):
        print(("----" * grid_dimensions[0])+"-")
        for x in range(0, grid_dimensions[0]):
            print("|", end="")
            if x == player_pos[0] and y == player_pos[1]:
                to_print = " P "
            else:
                to_print = "   "
            print(to_print, end="")
        print("|")
    print(("----"*grid_dimensions[0]) + "-")


def make_move(grid_dimensions: list[int], player_pos: list[int]) -> list[int]:
    """Function that lets the player make their move"""
    player_making_move = True

    while player_making_move:
        try:
            x_move = int(input("""Enter the horizontal move you would like to make.
A negative number will make you go left on the grid.
A positive number will make you go right on the grid.
"""))
            if (player_pos[0] + x_move) > (grid_dimensions[0] - 1) or (player_pos[0]+x_move) < 0:
                raise ValueError
            y_move = int(input("""Enter the vertical move you would like to make.
A negative number will make you go up on the grid.
A positive number will make you go down on the grid.
"""))
            if (player_pos[1] + y_move) > (grid_dimensions[1] - 1) or (player_pos[1]+y_move) < 0:
                raise ValueError
            player_making_move = False
        except (ValueError, TypeError):
            print("""You have entered a move that I do not understand or is invalid.
Let's start over.""")

    player_pos[0] += x_move
    player_pos[1] += y_move
    return player_pos


def game_update(grid: list[str], gold: int, chest_count: int, bandit_count: int,
                player_pos: list[int]) -> int:
    """
    This functions updates the game for when the player has finished their move.
    It will update the chest based on the number of visits the player has made.
    It will update the player gold based on what encounter occurs.
    It will update the number of chests and bandits if a chest turns into a bandit
    Finally, it returns the gold and number of chests and bandits
    """
    if grid[player_pos[1]][player_pos[0]] == "0":
        grid[player_pos[1]][player_pos[0]] = "1"
        gold += 10
    elif grid[player_pos[1]][player_pos[0]] == "1":
        grid[player_pos[1]][player_pos[0]] = "2"
        gold += 10
    elif grid[player_pos[1]][player_pos[0]] == "2":
        grid[player_pos[1]][player_pos[0]] = "B"
        gold += 10
        chest_count -= 1
        bandit_count += 1
    elif grid[player_pos[1]][player_pos[0]] == "B":
        gold = 0

    return grid, gold, chest_count, bandit_count


def show_stats(gold: int, chest_count: int, bandit_count: int, move_number: int) -> str:
    """Function that displays the current player stats and game stats to the player"""
    return f"""
-------------------
Gold: {gold}
Chests: {chest_count}
Bandits: {bandit_count}
Number of moves: {move_number}
-------------------
"""


# def play():

def main() -> None:
    """Function used to actually start the program"""
    game_is_active = True
    print("--- Treasure Hunt ---")
    player_name = input("""Greetings player...
What is your name?
""")
    print(f"""Nice to meet you {player_name}!
Welcome to Treasure Hunt
------------------------
     (1) Play Game
     (2) Quit Game
------------------------""")
    while game_is_active:
        play_or_quit_option = input(
            "Please enter the number of the option you would like.")
        if play_or_quit_option == "2":
            print(f"See you next time {player_name}!")
            game_is_active = False
            return
        if play_or_quit_option == "1":
            print(f"""So {player_name}, you would like to play the game?
Let's set the game options...""")
            dimensions = get_grid_size()
            print(dimensions)
            number_of_chests = get_chest_amount()
            number_of_bandits = get_bandit_amount()

            player_gold = 0
            number_of_moves = 0
            player_position = [0, (dimensions[1] - 1)]

            game_grid = create_grid(dimensions)
            game_grid = populate_grid(game_grid, number_of_chests, number_of_bandits,
                                      dimensions, player_position)

            game_not_end = True

            while game_not_end:
                show_grid(dimensions, player_position)

                player_position = make_move(
                    dimensions, player_position)
                number_of_moves += 1

                game_grid, player_gold, number_of_chests, number_of_bandits = game_update(
                    game_grid, player_gold, number_of_chests, number_of_bandits,
                    player_position)
                print(show_stats(player_gold, number_of_chests,
                      number_of_bandits, number_of_moves))

                if player_gold >= 100:
                    print(f"""Well done!!!
You have won the game.
You took: {number_of_moves}  moves"""
                    )
                    return
                if number_of_chests == 0:
                    print(f"""Unlucky! :(
You have lost the game.
You took: {number_of_moves} moves""")
                    return
        print("You have entered an invalid option.")


main()

dkqowkdoqwk
