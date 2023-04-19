file_path = "C:\\PythonPrj\\resources\\input1.txt"
# with open(file_path, 'a') as file:
#     file.write("This will be added to the next line\n")

with open(file_path, 'r') as my_file1:
    content = my_file1.read()

with open(file_path, 'a') as my_file:
    text = my_file.write("\n" + content)

my_file1.close()
my_file.close()
