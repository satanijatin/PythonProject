def find_positions(list, value):
    positions = []
    for i in range(len(list)):
        if list[i] == value:
            positions.append(i)
    return positions


my_list = [1, 2, 3, 4, 2, 5, 2]
value_to_find = 2
positions = find_positions(my_list, value_to_find)
print("Positions of", value_to_find, "in the list:", positions)
