x = {"name" : "John", "age" : 36}
print(type(x))

print(bool("abc"))

print(bool(0))

s = "input11A"
for i in s:
    if i.isalpha():
        print("True")

    elif i.isidentifier():
        print("True")
    elif i.isdigit():
        print("True")
    elif i.islower():
        print("True")
    elif i.upper():
        print("True")
    else:
        print("False")
