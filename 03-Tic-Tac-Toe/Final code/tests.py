game_state = input()
x_counter = game_state.count("X")
o_counter = game_state.count("O")
_counter = game_state.count("_")
gs = [x for x in game_state]

def print_game(game):
    print(f'''---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------''')

print_game(gs)

winner = [[gs[0], gs[1], gs[2]],  # 0 Row
          [gs[3], gs[4], gs[5]],  # 1 Row
          [gs[6], gs[7], gs[8]],  # 2 Row
          [gs[0], gs[4], gs[8]],  # 3 Diagonal
          [gs[6], gs[4], gs[2]],  # 4 Diagonal
          [gs[0], gs[3], gs[6]],  # 5 Column
          [gs[1], gs[4], gs[7]],  # 6 Column
          [gs[2], gs[5], gs[8]]]  # 7 Column
'''
if x_counter == o_counter + 2 or o_counter == x_counter + 2:
    print("Impossible")
elif ["X", "X", "X"] in winner and ["O", "O", "O"] in winner:
    print("Impossible")
elif ["X", "X", "X"] in winner:
    print("X wins")
elif ["O", "O", "O"] in winner:
    print("O wins")
elif _counter > 0:
    print("Game not finished")
else:
    print("Draw")
'''


# Replaces the index method. It doesn't return an Error if the item isn't found in a list
def linear_search(array, to_find):
    for i in range(0, len(array)):
        if array[i] == to_find:
            return i
    return -1
perma_coords = [["1", "1"], ["1", "2"], ["1", "3"],
                ["2", "1"], ["2", "2"], ["2", "3"],
                ["3", "1"], ["3", "2"], ["3", "3"]]
# Valid inputs without taking into account occupied coordinates
valid_coordinates = [x for x in perma_coords]

# Example game, to be replaced with input() as its value
perm_gs = [x for x in gs]

# Obtains the available coordinates, i.e. the unoccupied ones
def obtain_actual_valid_coordinates(game, valid_coordinates):
    # Tracks where's the last free space in the game given
    av_space_index_in_valid_coordinates = 0
    # Stores the indeces where there's no "X", nor "O"
    available_spaces_indeces = []
    while av_space_index_in_valid_coordinates != -1:
        av_space_index_in_valid_coordinates = linear_search(game, "_")
        if av_space_index_in_valid_coordinates != -1:
            available_spaces_indeces.append(av_space_index_in_valid_coordinates)
            game[av_space_index_in_valid_coordinates] = "R"

    # Var with the coordinates available to use in format [1, 1], as a list
    ultimate_val_coordinates = []
    for index in available_spaces_indeces:
        ultimate_val_coordinates.append(valid_coordinates[index])

    # Removes the free spaces from the original 9x9 available coordinates, to obtain
    # a list with the occupied spaces
    for coordinate in ultimate_val_coordinates:
        valid_coordinates.remove(coordinate)
    return ultimate_val_coordinates, valid_coordinates

# Analyzes the input to obtain unoccupied coordinates
def valid_input(valid_coordinates, perma_coords):
    user_coords = input("Enter the coordinates: ")
    # Checks if the input are not digits
    not_digit = not user_coords.replace(" ", "").isdigit()
    # Checks if the input is not within the 9x9 grid
    temp_var = user_coords.split()
    found = linear_search(perma_coords, temp_var)
    not_inside_grid = linear_search(perma_coords, temp_var) == -1
    # Checks if the input is not a free space in the grid
    not_free_space = linear_search(valid_coordinates, user_coords.split()) == -1
    if not_digit:
        print("You should enter numbers!")
        return valid_input(valid_coordinates, perma_coords)
    elif not_inside_grid:
        print("Coordinates should be from 1 to 3!")
        return valid_input(valid_coordinates, perma_coords)
    elif not_free_space:
        print("This cell is occupied! choose another one!")
        return valid_input(valid_coordinates, perma_coords)
    else:
        return user_coords.split()

def insert_move(coordinates, game):
    game_index_to_insert = linear_search(perma_coords, coordinates)
    game[game_index_to_insert] = "X"
    return game


# The occupied coordinates and unoccupied ones are assigned to their respective variables
valid_and_occupied_coordinates = obtain_actual_valid_coordinates(gs, valid_coordinates)
valid_coordinates = valid_and_occupied_coordinates[0]
occupied_coordinates = valid_and_occupied_coordinates[1]

# Checks the input given the spaces available in the grid
print_game(insert_move(valid_input(valid_coordinates, perma_coords), perm_gs))
