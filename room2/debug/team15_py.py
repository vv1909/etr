def reverse_list(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[-1-i])

    return new_list

print(reverse_list([1, 2, 3]))