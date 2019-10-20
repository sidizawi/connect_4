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

# AI: 

# Main:


# BODY:

