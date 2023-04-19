class Person:
    def __init__(self):
        print(f'Initiani a new person: {self}')


p = Person()

print(hex(id(p)))
