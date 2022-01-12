def main():
    side_num = int(input("Enter the number of sides you wnat to play with: "))
    row_grid = set_board(side_num)
    value_dict = value_dict_generator(row_grid)
    gameplay(row_grid, value_dict)

def value_dict_generator(rows):
    value_dict = {}
    count = 1
    for i in rows:
        inner_list = i
        for x in inner_list:
            value_dict[count] = str(x)
            count = count + 1
    return value_dict

def gameplay(row_grid, value_dict):
    gameplay = True
    dict = value_dict
    rows = row_grid
    user = "x"
    while gameplay == True:
        display_grid(rows, dict)
        if user == "x":
            user = "o"
        else:
            user = "x"
        user_input = int(input(f"{user}'s turn to choose a square: "))
        print()
        dict.update({user_input: user})
        victory_check(rows, dict)

def set_board(side):
    value_dict = {}
    rows = []
    val = 1
    for i in range(0, side):
        row_list = []
        for num in range(0, side):
            row_list.append(num+val) 
            value_dict[num+val] = str(f"{num+val}")
        rows.append(row_list)
        val = val + side
    return rows

def victory_check(row_grid, dict):
        rows = len(row_grid)
        row_list = []
        row_values = []
        column_list = []
        column_values = []
        up_diagonal_list = []
        down_diagonal_list = []
        diagonal_list = []
        for i in row_grid:
            row_list.append(row_grid.index(i))
            row_values.append(i)
            count = row_grid.index(i)
            inverse_count = rows-count-1
            for x in i:      
                if x == i[inverse_count]:
                    up_diagonal_list.append(x)
                    diagonal_list.append(up_diagonal_list)          
            for x in i: 
                if x == i[count]:
                    down_diagonal_list.append(x)
                    diagonal_list.append(down_diagonal_list)
        for i in row_list:
            column_list = [x[i] for x in row_values]
            column_values.append(column_list)
        diagonal_values = diagonal_list[:2]
        new_dict = dict
        row_number_list = []
        column_number_list = []
        diagonal_number_list = []
        for i in row_values:
            for x in i:
                row_number_list.append(new_dict[x])
        final_rows = [row_number_list[i:i+rows] for i in range(0, len(row_number_list), rows)]
        for i in column_values:
            for x in i:
                column_number_list.append(new_dict[x])
        final_columns = [column_number_list[i:i+rows] for i in range(0, len(column_number_list), rows)]
        for i in diagonal_values:
            for x in i:
                diagonal_number_list.append(new_dict[x])
        half = int(len(diagonal_number_list)/2)
        final_diagonals = [diagonal_number_list[half:], diagonal_number_list[:half]]
        for i in final_rows:
            if i.count(i[0]) == len(i):
                print("Good game. Thanks for playing!")
                quit()
        for i in final_columns:
            if i.count(i[0]) == len(i):
                print("Good game. Thanks for playing!")
                quit()
        for i in final_diagonals:
            if i.count(i[0]) == len(i):
                print("Good game. Thanks for playing!")
                quit()

def display_grid(row_grid, value_dict):
    rows = len(row_grid)
    dict = value_dict
    number_list = []
    for i in row_grid:
        for x in i:
            number_list.append(dict[x])
    number_rows = [number_list[i:i+rows] for i in range(0, len(number_list), rows)]
    for i in number_rows:
        row = i
        row_list = []
        for num in row:
            num_string = str(num)
            string = '{:^5}|'.format(num_string)
            row_list.append(string)
            string = ''.join(row_list) 
            length = len(string)
            return_string = string[:length] 
        print('|{:^10}'.format(return_string))
        row_list.clear() 

main()