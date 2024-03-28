# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:00:32 2024

@author: 157082
"""

# tup = (1,2,3,4,5)
# x = list(tup)
# x.append(7)
# y= tuple(x)
# print(y)
# #Another Solution

# u =tup+(7, 9)

# print(u)

#####################

# li= [1,2,3,4]
# x= 0
# for i in li:
#     x = x+i
# print(x)    
# # #########################
# li= [1,2,3,4]
# x= 1
# for i in li:
#     x = x*i
# print(x)

# ##################
# li = [30, 15, 3, 4, 5]

# smallest_number = li[0]

# for num in li:
#     if num < smallest_number:
#         smallest_number = num

# print( smallest_number)
# ###############################

# li = [30, 15, 3, 4, 5]

# largest_number = li[0]

# for num in li:
#     if num > largest_number:
#         largest_number = num

# print(largest_number)
################################

# lis= ["ma","he","er",4 ,9]
# k = 0
# for i in lis:
#     if isinstance(i, str):
#        k =k+1
# print(k)

# ##############################
# original_list = [1, 2, 3, 4, 5]
# cloned_list = original_list[:]
# print("Original List:", original_list)
# print("Cloned List:", cloned_list)
#####################################
# s ={0, 1, 3, 4, 5}
# s.remove(4)
# print(s)
#######################
# my_set = {10, 20, 30, 40, 50}

# max_value = None
# min_value = None

# for value in my_set:
#     if max_value is None or value > max_value:
#         max_value = value
#     if min_value is None or value < min_value:
#         min_value = value

# print("Maximum value in the set:", max_value)
# print("Minimum value in the set:", min_value)
################################################

# t = (10, 20, 30, 40)
# x= ("a","b","c","d")
# for z,y in zip(t,x):
#     s={y:z}
#     print(s)
#################################################
# t = (10, 20, 30, 40)
# z=list(t)
# z.reverse()
# z=tuple(z)
# print(z)
##########################################

# l=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# m = [i[:-1]+(100,) for i in l]

# print(m)
##########################################

# ar_name = "%%6student_name ^ %#"
# illegal_chars = "0123456789!@#$%^&*()-+=[]{}|\;:"",.<>/?~"
# for i in illegal_chars:
#     ar_name=ar_name.replace(i,"")
# print(ar_name)

############################################

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# for i in numbers:
#     if i==0:
#         print("Zero number: ",i)
#     elif i%2==0:
#         print("Even number: ",i)
#     else:
#         print("Odd number: ",i)
# #####################################
            
# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#####################################





































































































