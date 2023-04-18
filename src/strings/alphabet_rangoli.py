# def print_rangoli(size):
# your code goes here

N = 5
# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using loop
res = ""
for idx in range(97, 97 + N):
    res = res + chr(idx)

# printing result
print("Alphabets till " + str(N) + " are : " + str(res))


def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in {'A', 'E', 'I', 'O', 'U'}:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)
    if stuart == kevin:
        print('Draw')
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Kevin', kevin)


s = "abcd".upper();
minion_game(s);
