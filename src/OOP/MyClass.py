class MyClass:
    language = 'Python'
    version = '3.9'


print(MyClass.version)
print(MyClass.language)
print(MyClass.__class__)
print(MyClass.__name__)
print(MyClass.__hash__(MyClass))
print(getattr(MyClass, 'xxx', 'n/a'))


def say_hallo():
    print("say hello")


say_hallo()

print(MyClass.__dict__)

try:
    print(getattr(MyClass, 'xxx'))
except AttributeError:
    print("nu exista aceasta proprietate")
