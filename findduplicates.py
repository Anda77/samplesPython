some_list = ['a', 'b', 'c', 'b', 'n', 'm', 'm']

duplicates = []

for value in some_list:
    if (some_list.count(value) > 1):
        if value not in duplicates:
            duplicates.append(value)


print(duplicates)