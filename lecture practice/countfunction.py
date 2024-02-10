def count_occurrences(lst, element):
    occurrences = 0
    for item in lst:
        if item == element:
            occurrences += 1
    return occurrences


my_list = [1, 2, 3, 4, 1, 2, 1, 1]
element_to_count = int(input("Enter Number to be Count : "))
print(f"The element {element_to_count} occurs {count_occurrences(my_list, element_to_count)} times.")
