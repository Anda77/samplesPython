for item in (1, 2, 3, 4, 5):
    for i in ['a', 'b', 'c']:
        print(item, i)

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

counter = 0
for item in my_list:
    counter = counter + item

print(f'counter', {counter})
