# matrix=[
#     [1,2,3,4,5],
#     [6,7,8,9,10]
#     [11,12,13,14,15]
#     [16,17,18,19,20]
#     [21,22,23,24,25]
# ]
from sys import flags


def print_matrix(matrix):
    #the function prints the items in matrix
    for i in range(5):
        print(matrix[i])


def sum_marix_itemes(matrix):
    #the function culacte the sum of all the items
    sum_all_items=0
    for row in matrix:
        for cloe in matrix:
            sum+=[row][cloe]
    return sum_all_items

def slant_sum_of_matrix(matrix):
    #the function culacte all the items who in the main slant
    slant_sum=0
    for i in range(len(matrix)):
        slant_sum=matrix[i][i]
    return slant_sum








#ex4
def turn_all_to_empty():
    # The function initializes all members to empty.
    matrix=[]
    for i in range(5):
        arr_for_line = []
        for j in range(5):
            arr_for_line.append("EMPTY")
        matrix.append((arr_for_line))
        arr_for_line=[]
    return matrix

def check_user_input(user_row, user_cloe):
    #the function check if the input of the user is ok
    flag=False
    if(0<user_row<=5 and 0<user_cloe<=5):
        flag= True
    return flag

def where_is_boat(matrix):
    #ask for submarine place
    print("Hi, for beginning the game you have to enter the submarine place:")
    boat_row = int(input("Enter row: "))
    boat_cloe = int(input("Enter cloe: "))
    #ask again, also if it's bigger than 3 because we nees to puy three submarine
    while( not(0<boat_row<=3 and 0<boat_cloe<=3)):
        boat_row = int(input("Enter row again: "))
        boat_cloe = int(input("Enter cloe again: "))

    matrix[boat_row-1][boat_cloe-1]="SUBMARINE"
    matrix[boat_row][boat_cloe-1]="SUBMARINE"
    matrix[boat_row+1][boat_cloe-1]="SUBMARINE"
    return matrix



def cheack_user_sucsees(matirx, row_guess, cloe_guess):
    is_sucsess= False
    if(matirx[row_guess-1][cloe_guess-1]=="SUBMARINE"):
        is_sucsess=True
    return is_sucsess




#צריך לזכור:
#הערכים ההתחלתים הם 1,1
#אם המשתמש הכניס קלא לא תקין לא שואלים שוב פעם, פשוט הוא עובר לתור הבא שלו

#main
matrix=turn_all_to_empty()

matrix=where_is_boat(matrix)

print_matrix(matrix)

# user_row= int(input("Hi, enter row guess: "))
# user_cloe= int(input("Hi, enter clow guess: "))
#
# number_of_guess=0
#
# player_sucsess=False
#
# input_is_okay=check_user_input(user_row, user_cloe)
#





