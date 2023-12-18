liste = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 9, 9, 10]

print(list(({value: liste.count(value) for value in liste}).keys()))