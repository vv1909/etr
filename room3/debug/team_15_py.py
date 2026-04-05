def sort_custom(lst, key):
    return sorted(lst, key=lambda x: x[key])

print(sort_custom([{'a': 3}, {'a': 1}, {'a': 2}], 'a'))