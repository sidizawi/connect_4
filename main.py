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
        print(i+1, '|', end=" ")
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                print(' ', end=' ')
            elif mat[i][j] == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print('|')
    print('    A B C D E F G')

# Check functions:
def check_rows(mat, player):
    res = False
    for row in range(len(mat)-1, -1, -1):
        for col in range(int(len(mat[0])/2)+1):
            if mat[row][col] == player and mat[row][col+1] == player and mat[row][col+2] == player and mat[row][col+3] == player:
                res = True
    return res

def check_columns(mat, player):
    res = False
    for col in range(len(mat[0])):
        for row in range(len(mat)-1, int(len(mat)/2), -1):
            if mat[row][col] == player and mat[row-1][col] == player and mat[row-2][col] == player and mat[row-3][col] == player:
                res = True
    return res

# AI: 

# Main:


# BODY:

