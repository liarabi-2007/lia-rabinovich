import random


def print_matrix(matrix):
    # the function prints the items in matrix
    for i in range(4):
        print(matrix[i])


def full_with():
    matrix = []
    for i in range(4):
        arr_for_line = []
        for j in range(4):
            arr_for_line.append(-1)
        matrix.append((arr_for_line))
        arr_for_line = []
    return matrix


def make_matrix(matrix):
    # draw number to tow and cloe
    count_put = 0
    row_random = 0
    cloe_random = 0
    i = 0
    while (count_put != 16):
        for j in range(2):
            row_random = random.randint(0, 3)
            cloe_random = random.randint(0, 3)

            while ((matrix[row_random][cloe_random] != -1)):
                row_random = random.randint(0, 3)
                cloe_random = random.randint(0, 3)
            matrix[row_random][cloe_random] = i
            count_put += 1
        i = i + 1


    return matrix


matrix = []
matrix = full_with()
print_matrix(matrix)

matrix = make_matrix(matrix)
print_matrix(matrix)

# for i in range(16):
#     if(matrix[row_random][cloe_random]==-1):
#         for j in range(8):
#           for o in range(2):
#               row_random = random.randint(0, 4)
#               cloe_random = random.randint(0, 4)
#
