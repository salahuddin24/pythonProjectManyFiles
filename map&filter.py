# map syntex
# map(function, object/list)
from lamdaFunction import result

# def square(x) :
#     return  x*x
# nums = [1, 2, 3, 4, 5]
#
# result = list(map(square, nums))
# print(result)


# fiter function
# filter(function, list/object)
nums = [1,2,3,4,5,6]
result = list(filter(lambda x : x%2==0, nums))
print(result)



















