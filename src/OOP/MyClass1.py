class MyClass1:
    pass


setattr(MyClass1, 'test', 10)

m = MyClass1()

print(MyClass1.__dict__)

print(isinstance(m, str))

print(isinstance(m, object))

print(isinstance(m, MyClass1))
