# reading file ---syntex ---
#open("file name" , "mode")
# write korar jonno = "w" ar read korar jonno = "r"

# file = open("student.txt", "r")
# print(file.readable())
# text = file.read()
# print(text)
# size = len(text)
# print(size)
#
# for line in file :
#     print(line)

   #append and write
# file = open("student.txt", "a") # a for append
# file.write("\n Sadi - Lecturer of physics")

file = open("student.txt", "w") # w for write || shodu write dile sheta over write kore falbe
file.write("\n Out department head is Saif sir")

file.close()






















