# Library function => print(), input(), abs() etc
# user define function => create user

# syntex
# def funcName(parametre) :
#     to do print


# def add(x, y) :
#     sum = x + y
#     print(sum)
#
# add(12, 23) # calling function
#
# def addition(x, y, z ) :
#     sum = x + y + z
#     print(sum)
# addition(12, 3, 23)
#
# def message() :
#     print("no message ")
#
# message()

# def large(a, b) :
#     if a>b :
#         return a
#     else:
#         return b
#
# print(large(12, 42))
#
# #### xagrs
# def add(*numbers) :
#     sum = 0
#     for num in numbers :
#         sum = sum + num
#     print(sum)
#
# add(23, 42)
# add(23, 4, 23, 43)
#
#

### xxargs
def student(**details) :
    print(details)
    print(details["id"])
    print(details["name"])

student(id=101, name="Salah Uddin")



























