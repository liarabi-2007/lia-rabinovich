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


#
# #main
# #turn all to empty
# matrix=turn_all_to_empty()
# #locate thr boat
# matrix=where_is_boat(matrix)
#
# print_matrix(matrix)
#
# number_of_guess=0

#turn true or false if the iput of the user is okay

# player_sucsess=False
#
# while(player_sucsess==False ):
#     user_row = int(input("Hi, enter row guess: "))
#     user_cloe = int(input("Hi, enter clow guess: "))
#     input_is_okay = check_user_input(user_row, user_cloe)
#     player_sucsess=cheack_user_sucsees(matrix,user_row, user_cloe)
#     if(input_is_okay):
#         if (player_sucsess==True):
#             number_of_guess+=1
#             print("number of guess= ",number_of_guess)
#             print("Congratulations, YOU SUCESS")
#         else:
#             number_of_guess+=1
#
#     else:
#         ("this guess not count as a turn, enter another guesses")



def turn_all_to_O():
    # The function initializes all members to o.
    matrix=[]
    for i in range(5):
        arr_for_line = []
        for j in range(5):
            arr_for_line.append("O")
        matrix.append((arr_for_line))
        arr_for_line=[]
    return matrix

def user_choose_two_point():
    #the function recive 2 pints for each place
    print("Hi, for beginning the game you have to enter 2 point to where the boat place:")
    print("for the first point....")

    boat_row_point1=int(input("Enter row of the boat start: "))
    boat_cole_point1=int(input("Enter cole of the boat start: "))

    while(not (1<boat_row_point1<=5 or 1<boat_cole_point1<=5)):
        boat_row_point1 = int(input("Enter row of the boat start: "))
        boat_cole_point1 = int(input("Enter cole of the boat start: "))

    boat_row_point2 = int(input("Enter row of the boat end: "))
    boat_cole_point2 = int(input("Enter cole of the boat end: "))

    while (not (1 < boat_row_point2 <= 5 or 1 < boat_cole_point2 <= 5)):
        boat_row_point2 = int(input("Enter row of the boat start: "))
        boat_cole_point2 = int(input("Enter cole of the boat start: "))

def who_locate_more_less(x,y):
    if(x<y):
        return x
    else:
        return y

def who_locate_more_left(a,b):
    if(b>a):
        return a
    else:
        return b


def is_it_slant(row_boat1, cloe_boat1, row_boat2, cloe_boat2):
    #the function recive to points and return true or false id the points creat slants
    is_slant=False
    if(row_boat1!=row_boat2 and cloe_boat1!=cloe_boat2):
        is_slant=True
    return is_slant

def locate_boat(row_boat1, cloe_boat1, row_boat2, cloe_boat2, matrix_of_manger):
  #the function put in the manegr matrix the s sigh
    more_high_in_number=who_locate_more_less(row_boat1,row_boat2)
    more_left_in_number=who_locate_more_left(cloe_boat2,cloe_boat1)

    if(is_it_slant(row_boat1, cloe_boat1, row_boat2, cloe_boat2)):#if it is slant==true
        rows_number=abs(row_boat2-row_boat1)

        for i in range(rows_number+1):
            matrix_of_manger[i][more_left_in_number] = 's'
            more_left_in_number+=1
    elif (cloe_boat1==cloe_boat2):
        rows_number=abs(row_boat2-row_boat1)

        for i in range(rows_number):
            matrix_of_manger[i][cloe_boat2] = 's'
    elif(row_boat2==row_boat1):
        cloes_numbers=abs(cloe_boat2-cloe_boat1)
        for i in range(cloes_numbers):
            matrix_of_manger[row_boat2][i]="S"


    return matrix_of_manger










#main
def main():
    matrix_manger=turn_all_to_O()
    matrix_user=matrix_manger
    number_of_guess=0



    boat_row_point1=int(input("Enter row of the boat start: "))
    boat_cole_point1=int(input("Enter cole of the boat start: "))

    boat_row_point2 = int(input("Enter row of the boat end: "))
    boat_cole_point2 = int(input("Enter cole of the boat end: "))

    is_one_proper=check_user_input(boat_row_point1-1,boat_row_point2-1)
    is_two_proper=check_user_input(boat_row_point1-1,boat_row_point2-1)

    matrix_manger=locate_boat(boat_row_point1-1,boat_cole_point1-1,boat_row_point2-1,boat_cole_point2-1,matrix_manger)

    player_sucsess = False

    while (player_sucsess == False):
        boat_row_point1 = int(input("Enter row of the boat start: "))
        boat_cole_point1 = int(input("Enter cole of the boat start: "))

        boat_row_point2 = int(input("Enter row of the boat end: "))
        boat_cole_point2 = int(input("Enter cole of the boat end: "))

        is_one_proper = check_user_input(boat_row_point1 - 1,boat_row_point2 - 1)
        is_two_proper = check_user_input(boat_row_point1 - 1,boat_row_point2 - 1)

        input_is_okay = check_user_input(user_row, user_cloe)
        player_sucsess = cheack_user_sucsees(matrix, user_row, user_cloe)
        if (input_is_okay):
            if (player_sucsess == True):
                number_of_guess += 1
                print("number of guess= ", number_of_guess)
                print("Congratulations, YOU SUCESS")
            else:
                number_of_guess += 1

        else:
            ("this guess not count as a turn, enter another guesses")


main()













