import string

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

def solve(s):
    return s.title()

print(solve("1 w 2 r 3g"))

str1 = string.ascii_lowercase[:3]

list1 = (list(str1))

print(str1[len(str1)-1])


def wrap(string, max_width):
    len1 = len(string)
    return len1

print(wrap("vvvvvvvvvvv", 8))

def mutate_string(string, position, character):
    convert = list(string)
    convert[position] = character
    return ''.join(convert)


print(mutate_string("mmmm", 1, "k"))