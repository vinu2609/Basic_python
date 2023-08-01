# Write a program to print multiplication table of a given number using for loop.
# num = int(input("Enter the number"))
# for i in range(1, 11):
#     print(str(num) + "X" + str(i) + "=" + str(i*num))

    
# Atempt problem 1 using while loop.
# i = 1
# while i<=10:
#     print(str(3) + "X" + str(i) + "=" + str(i*3))
#     i = i+1

# Write a program to greet all the person names stored in a list l1 and which starts with s.

# l1 = ["Harry","Vini","Vinu","Yashi"]
# for name in l1:
#     if name.startswith("V"):
#         print(" Hello " +  name)

#  Write a program to find whether a given number is prime or not.
# num = int(input("Enter your number"))
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False

# if prime:
#     print("This number is prime")
# else:
#     print("This number is not prime")

# Write a program to find the sum of first n natural numbers using while loop.
# number = int(input("enter your number:"))
# i = 1
# total = 0
# while i<=number:
#     total = total + i
#     i = i + 1
# print("The sum of natural number from 1 to {0} = {1}".format(number,total))  

# Write a program to calculate the factorial of a given number using for loop.
# n! = 1 X 2 X 3 X 4 X 5 X..............X n
# 5! = 1 X 2 X 3 X 4 X 5

# num = int(input("Enter the number:")) 
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print (f"The factorial of this number is {factorial}")

# n = 4

# for i in range(4):
#     print("*" * (i+1))

# Write a program to print multiplication table of n using for loop in reversed order.
num = int(input("Enter the number"))
for i in range(11, 1):
    print(str(i*num) + "=" + str(i) + "X" + str(num))

    # print(str(num) + "X" + str(i) + "=" + str(i*num))

    print(str(i*num) + "=" + str(i) + "X" + str(num))
            