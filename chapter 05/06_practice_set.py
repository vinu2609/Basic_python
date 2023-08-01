# Write a python program to create a dictionary of hindi words with values as their english translation provide users with an option to look it up

myDict = {
    "pankha" : "fan",
    "kursi" : "chair",
    "dabba" : "box",
}
print("options are",myDict.keys())
a = input("enter the hindi word\n")
print("the meaning of your word is:",myDict[a])

#  below line will not throw an error if the key is not present in the dictionary.
print("the meaning of your word is",myDict.get(a))

# Write a python program to input eight numbers from the users and display all the unique numbers (onces)
num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
num3 = int(input("enter number 3"))
num4 = int(input("enter number 4"))
num5 = int(input("enter number 5"))
num6 = int(input("enter number 6"))
num7 = int(input("enter number 7"))
num8 = int(input("enter number 8")) 
a = {num1,num2, num3, num4, num5, num6, num7, num8}
print(a)

# Can we have a set with 18(int) and "18"(str) as a value in it.
s = {18, "18"}
print(len(s))
print(s)

# What will be the length of following set s.
s = {20, 20.0,"20"}
print(len(s))
print(s)

# s = {}.....What is the type of s ?
s = {}
print(type(s))

# Create an empty dictionary. Allow 4 friends to enter their favourite languages as values and use keys as their names. Assume that the names are unique.
favLang = {}
a = input("Enter your favorite language Alisha\n")
b = input("Enter your favorite language Monika\n")
c = input("Enter your favorite language Harshita\n")
d = input("Enter your favorite language Vini\n")
favLang['Alisha'] = a
favLang['Monika'] = b
favLang['Harshita'] = c
favLang['Vini'] = d
print(favLang)

# If names are two friends are same; what will happen to the program in problem 6 ?
favLang = {}
a = input("Enter your favorite language Alisha\n")
b = input("Enter your favorite language Monika\n")
c = input("Enter your favorite language Alisha\n")
d = input("Enter your favorite language Vini\n")
favLang['Alisha'] = a
favLang['Monika'] = b
favLang['Alisha'] = c
favLang['Vini'] = d
print(favLang)

# If languages of two friends are same; What will happen to the program in problem 6 ?
favLang = {}
a = input("Enter your favorite language Alisha\n")
b = input("Enter your favorite language Monika\n")
c = input("Enter your favorite language Harshita\n")
d = input("Enter your favorite language Vini\n")
favLang['Alisha'] = a
favLang['Monika'] = b
favLang['Harshita'] = c
favLang['Vini'] = d
print(favLang)

# Can you changes the values inside a list which is contained in set s.....s = {8,7,12,"harry",[1,2]}
s = {8,7,12,"harry",[1,2]} #....throw error because this question is wrong.
print(type(s))



