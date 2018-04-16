# Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful,
# smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies
# at the same time, after all! In order to make sure that everyone working for her is
# sufficiently quick-witted, Commander Lambda has installed new flooring outside the
# henchman dormitories. It looks like a chessboard, and every morning and evening you have
# to solve a new movement puzzle in order to cross the floor. That would be fine if you got
# to be the rook or the queen, but instead, you have to be the knight. Worse, if you take
# too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP
# doomsday device!

# To help yourself get to and from your bunk every day, write a function called
# answer(src, dest) which takes in two parameters: the source square, on which you start,
# and the destination square, which is where you need to land to solve the puzzle.
# The function should return an integer representing the smallest number of moves it will
# take for you to travel from the source square to the destination square using a chess
# knight's moves (that is, two squares in any direction immediately followed by one square
# perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and
# destination squares will be an integer between 0 and 63, inclusive, and are numbered
# like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) src = 19
#     (int) dest = 36
# Output:
#     (int) 1

# Inputs:
#     (int) src = 0
#     (int) dest = 1
# Output:
#     (int) 3

# lower_left_bound = [0, 8, 16, 24, 32, 40, 48, 56]
# upper_right_bound = [7, 15, 23, 31, 39, 47, 55, 63]
# upper_bound = [56, 57, 58, 59, 60, 61, 62, 63]
# lower_bound = [0, 1, 2, 3, 4, 5, 6, 7]


# minus_left = [-17, -10]
# minus_right = [-15, -6]
# plus_left = [6, 15]
# plus_right = [10, 17]

# far_down_minus_left = -17
# far_left_minus_left = -10
# far_down_minus_right = -15
# far_right_minus_right = -6

# far_up_plus_left = 15
# far_left_plus_left = 6
# far_up_plus_right = 17
# far_right_plus_right = 10


# -17, -15, -10, -6, 6, 10, 15, 17

def make_board():
    i = 0
    board = []
    while i <= 63:
        row = [j for j in range(i, i + 8)]
        i += 8
        board.append(row)
    return board

def find_coordinates(num):
    x = int(num / 8)
    y = num % 8
    return x, y

def answer(curr, goal):
    board = make_board()
    moves = [curr]
    counter = 1
    while True:
        new_moves = []
        for curr in moves:
            cx, cy = find_coordinates(curr)
            for i in [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]:
                mx = cx + i[0]
                my = cy + i[1]
                if mx >= 0 and my >= 0 and mx <= 7 and my <= 7:
                    move = board[mx][my]
                    if move == goal:
                        return counter
                    elif move not in new_moves:
                        new_moves.append(move)
        moves = new_moves
        counter += 1


print(answer(0, 31))

