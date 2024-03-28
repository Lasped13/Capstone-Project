"""
This is a program that allows the user to play a mini Treasure Hunt Game
This will be done on a grid where the user will enter coordinates to move around the grid.
The mechanics are similar to Minesweeper in the sense that some grid spaces will give
them points whereas others will reduce their points
"""


import random


def create_grid(x_dimension, y_dimension):
    """Function that creates the grid in which the game is played on"""
    grid = [[" " for x in range(x_dimension)] for y in range (y_dimension)]
    return grid


def set_chests_and_bandits(grid, x_dimension, y_dimension, x_player_position, y_player_position ):
    """Function that sets chests and bandits on the board"""
    x = random.randint(0, x_dimension-1)
    y = random.randint(0, y_dimension-1)
    if (x == x_player_position and y_player_position) or (grid[y][x] != " "):
        ...


def populate_grid(grid, chest_count, bandit_count, x_dimension, y_dimension, x_player_position, y_player_position):
    for number_of_chests in range(0, chest_count):
        grid = set_chests_and_bandits(grid, x_player_position, y_player_position, x_dimension, y_dimension)
    for number_of_bandits in range(0, bandit_count):
        grid = set_chests_and_bandits(grid, x_player_position, y_player_position, x_dimension, y_dimension)
    return grid


def show_grid()
    for y in range(0, y)
