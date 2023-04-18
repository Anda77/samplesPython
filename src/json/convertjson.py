import json

# a Python object (dict):
# x = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

x = open("C:\\PythonPrj\\resources\\test.json", "r")

# convert into JSON:
y = json.dumps(x.read())

print(y)
print(type(y))

print(y[0])
print(y[1])

y1 = json.loads(y)

print(type(y1))

# the result is a JSON string:
print(y1)
print(y1[0])
print(y1[1])
