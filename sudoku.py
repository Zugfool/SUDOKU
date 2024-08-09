import random; import numpy as np;import os;import solver as sd

os.system('cls' if os.name == 'nt' else 'clear')

all_numbers = list(range(1, 10))
error = 0

sudoku = np.zeros((9, 9),dtype=int)
row = 0

while row<9:
    new_row = []
    check_y = sd.BOX(row)
    
    for column in range(9):
        already_used = []
        control1 = list(sudoku[:,column])
        control2 = list(sudoku[row,:])
        for column_value in control1: 
            already_used.append(column_value)
        for row_value in control2:
            already_used.append(row_value)
        
        check_x = sd.BOX(column)

        box = sudoku[check_y[0]:check_y[1],check_x[0]:check_x[1]]
        box = box.reshape(1,9);box_list = box.tolist();box_list = box_list[0]

        for box_value in box_list:   
            already_used.append(box_value)      

        pickable_numbers = []

        for option in all_numbers:
            if option not in already_used:
                pickable_numbers.append(option)

        if len(pickable_numbers) == 0:
            sudoku[row] = [0,0,0,0,0,0,0,0,0]
            row = row-1
            error += 1
            if error == 100:
                sudoku = np.zeros((9, 9),dtype=int)
                print(f"Trying again because of random errors.Error was in {row}th row.")
                row=0;error = 0
            break
        else:
            number = sd.pick(pickable_numbers)
            sudoku[row,column] = number
    row += 1

sudoku = sudoku.reshape(9,9)

desire = str(input("What do you want the hardness of your sudoku: ")); desire = desire.capitalize()
amount,rep = sd.hardness(desire)

relocationg = -1
repeat = True

while repeat == True:
    relocationg += 1
    choosing = 0
    shown_numbers = []
    while choosing < amount:
        shown_location = []
        for j in range(2):
            x = random.randint(0,8)
            shown_location.append(x)
        if shown_location not in shown_numbers:
            shown_numbers.append(shown_location)
            choosing += 1
    repeat = False

    first_list = [0,0,0,0,0,0,0,0,0];second_list = [0,0,0,0,0,0,0,0,0]
    for x in shown_numbers:
        first = x[0];second = x[1]
        first_list[first] += 1;second_list[second] +=1
    for value in first_list:
        if value < rep:
            repeat = True
    for value in second_list:
        if value < rep:
            repeat = True

asked_sudoku = np.zeros((9, 9),dtype=int)
for number in shown_numbers:
    asked_sudoku[number[0],number[1]] = sudoku[number[0],number[1]] 

print(f"It took {error} errors and {relocationg} replacements.")
print(asked_sudoku);print("\n")
ans,execution = sd.solve_sudoku(asked_sudoku)

if ans == True and execution < 20:
    print(f"It took {execution} to solve. \n" , sudoku)