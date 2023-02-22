with open('resources/test.txt', 'r+') as my_file:
    text = my_file.write('hey it ''s  me')
    print(text)
my_file.close()
