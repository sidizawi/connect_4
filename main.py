"""
author : Zawi, Sidi M.
github : sidizawi
"""
# IMPORTS:


# FUNCTIONS:
# Matrix:
def matrix():
    mat = []
    for i in range(6):
        m = []
        for j in range(7):
            m.append(0)
        mat.append(m)
    return mat

# Display:
def display(mat):
    for i in range(len(mat)):
        print('|', end=" ")
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                print(' ', end=' ')
            elif mat[i][j] == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print('|')
    print('  1 2 3 4 5 6 7')

# Check functions:
def check_rows(mat, player): # check rows
    res = False
    for row in range(len(mat)-1, -1, -1):
        for col in range(int(len(mat[0])/2)+1):
            if mat[row][col] == player and mat[row][col+1] == player and mat[row][col+2] == player and mat[row][col+3] == player:
                res = True
    return res

def check_columns(mat, player): # check columns
    res = False
    for col in range(len(mat[0])):
        for row in range(len(mat)-1, int(len(mat)/2)-1, -1):
            if mat[row][col] == player and mat[row-1][col] == player and mat[row-2][col] == player and mat[row-3][col] == player:
                res = True
    return res

def check_diag(mat, player): # check diagonals
    res = False
    for row in range(len(mat)-1, int(len(mat)/2)-1, -1):
        for col in range(int(len(mat[0])/2)+1):
            if mat[row][col] == player and mat[row-1][col+1] == player and mat[row-2][col+2] == player and mat[row-3][col+3] == player:
                res = True
    return res

def check(mat, player):
    res_row = check_rows(mat, player)
    res_col = check_columns(mat, player)
    res_diag = check_diag(mat, player)
    res = False
    if res_col or res_row or res_diag:
        res = True
    return res

def check_3_tokens(mat):
    sol = []
    for row in range(len(mat)-1, -1, -1):
        for col in range(int(len(mat[0])/2)+1):
            if mat[row][col] == 1 and mat[row][col+1] == 1 and mat[row][col+2] == 1 and mat[row][col+3] == 0:
                sol.append((row, col+3))
            elif mat[row][col] == 1 and mat[row][col+1] == 1 and mat[row][col+2] == 0 and mat[row][col+3] == 1:
                sol.append((row, col+2))
            elif mat[row][col] == 1 and mat[row][col+1] == 0 and mat[row][col+2] == 1 and mat[row][col+3] == 1:
                sol.append((row, col+1))
            elif mat[row][col] == 0 and mat[row][col+1] == 1 and mat[row][col+2] == 1 and mat[row][col+3] == 1:
                sol.append((row, col))
    for col in range(len(mat[0])):
        for row in range(len(mat)-1, int(len(mat)/2)-1, -1):
            if mat[row][col] == 1 and mat[row-1][col] == 1 and mat[row-2][col] == 1 and mat[row-3][col] == 0:
                sol.append((row-3, col))
            elif mat[row][col] == 1 and mat[row-1][col] == 1 and mat[row-2][col] == 0 and mat[row-3][col] == 1:
                sol.append((row-2, col))
            elif mat[row][col] == 1 and mat[row-1][col] == 0 and mat[row-2][col] == 1 and mat[row-3][col] == 1:
                sol.append((row-1, col))
            elif mat[row][col] == 0 and mat[row-1][col] == 1 and mat[row-2][col] == 1 and mat[row-3][col] == 1:
                sol.append((row, col))
    for row in range(len(mat)-1, int(len(mat)/2)-1, -1):
        for col in range(int(len(mat[0])/2)+1):
            if mat[row][col] == 1 and mat[row-1][col+1] == 1 and mat[row-2][col+2] == 1 and mat[row-3][col+3] == 0:
                sol.append((row-3, col+3))
            elif mat[row][col] == 1 and mat[row-1][col+1] == 1 and mat[row-2][col+2] == 0 and mat[row-3][col+3] == 1:
                sol.append((row-2, col+2))
            elif mat[row][col] == 1 and mat[row-1][col+1] == 0 and mat[row-2][col+2] == 1 and mat[row-3][col+3] == 1:
                sol.append((row-1, col+1))
            elif mat[row][col] == 0 and mat[row-1][col+1] == 1 and mat[row-2][col+2] == 1 and mat[row-3][col+3] == 1:
                sol.append((row, col))
    return sol

# AI: 
def Ai(mat):
    pass

# Main functions:
def change_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def fill_mat(mat, player):
    col = input('player 1 >')
    while mat[0][col] != 0:
        col = input('This column is full')
    i = 5
    while i>= 0:
        if mat[i][col] == 0:
            mat[i][col] = player
            i = -1
        i -= 1
    return mat

def main():
    mat = matrix()
    display(mat)
    player = 1
    res = False
    i = 1
    while not res and i <= 49:
        if player == 1:
            mat = fill_mat(mat, player)
        else:
            mat = Ai(mat)
        res = check(mat, player)
        if res and player == 1:
            print('Bravo, you won')
        elif res:
            print('Game Over, AI won')
        elif i == 49:
            print('DRAW!')
        player = change_player(player)
        i += 1

# BODY:
if __name__ == '__main__':
    main()
