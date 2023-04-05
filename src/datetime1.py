from datetime import datetime

datetime_str = '09/19/22'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')

print(type(datetime_object))
print(datetime_object)  # printed in default format
