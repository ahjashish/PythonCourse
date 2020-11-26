# my_file = open('happy/test.txt')
# print(my_file)
# try:
#     value = my_file.read()
#     num = int(value)
# except ValueError:
#     print(f"Only numbers allowed {int(value)}")
# print(my_file.read())
#
# print(my_file.read())   # it won't be printing anything. because the cursor is at the end of the file.
#
# print("Seek 0")
# my_file.seek(0)     # we reset the cursor to the initial position.
#
# print(my_file.read())   # and so we can now read the file from the initial position till end.
#
# print("Seek 0")
# my_file.seek(0)
# print(my_file.readline())   # reads a line and stop the cursor
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# print("Seek 0")
# my_file.seek(0)
#
# print(my_file.readlines()) # store all the lines in a list
# print(my_file.readlines())
#
# finally:
#     print("Still closing the file")
#     my_file.close()

# with open("happy\happy.txt", mode='a') as my_file:
#     text = my_file.write("I am HAPPY!")
#     print(text)  # it prints the no. of letters written into the file

# with open("happy/happy.txt", mode='r') as my_file:
#     print(my_file.read())

# with open(".\happy\happy.txt", mode='a') as my_file:
#     text = my_file.write("I am HAPPY!")
#     print(text)  # it prints the no. of letters written into the file
#
# with open("E:\\Udemy Courses\\Python - Zero to Mastery\\Exercise\\File IO\\happy\\happy.txt", mode='r') as my_file:
#     print(my_file.read())