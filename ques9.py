#Max element in a list
def find_max_element(lst):
    max_element = lst[0]     # assume first element is maximum

    for num in lst:          # check each element
        if num > max_element:
            max_element = num

    return max_element


numbers = [3, 7, 2, 9, 5]
print(find_max_element(numbers))