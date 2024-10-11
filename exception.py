# exception = run time error
from multiprocessing.managers import Value

# num2 = int(input("Enter a number : "))
# result = 20 / num2
# print(result)

# try:
#     list = [20, 0, 30]
#     result = list[0] / list[3]
#     print(result)
#     print("Done")
# # except ZeroDivisionError:
# #     print("Zero Division Error")
# # except IndexError :
# #     print("index error")
#
# #multiple exception in line
# except (ValueError, ZeroDivisionError, IndexError) :
#     print("you have entered incorrect input .")
#
#
# finally:
#     print("successfully done")
#

# def voter(age) :
#     if age<18 :
#         raise ValueError("Invalid Voter")
#     return "you are allowed to vote"
#
# try:
#     print(voter(17))
#     print(voter(22))
# except ValueError as e:
#     print(e)


#swapping --- man binimoy kora

a = 20
b = 30

temp = a
a = b
b = temp

print("a =", a , " b = ", b)


















