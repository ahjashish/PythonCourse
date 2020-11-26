import datetime
from time import time
from array import array

print(datetime.time())
# print(datetime.time(55,45,2))   # hour must be between 0 to 23
print(datetime.time(5,45,2))

print(datetime.date.today())

print(time())   # time in unix code

arr = array('i', [1,2,3])
print(arr)
print(arr[0])