# Write a python program to find greatest of four numbers entered by the user.
# num1 =int (input("enter number 1:"))
# num2 =int (input("enter number 2:"))
# num3 =int (input("enter number 3:"))
# num4 =int (input("enter number 4:"))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4


# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + "is gretest")
# else:
#     print(str(f2) + "is greatest")    

# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take make as an input from the user.
# sub1 = int(input("Enter first subject marks"))
# sub2 = int(input("Enter second subject marks"))
# sub3 = int(input("Enter third subject marks"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail because you have less than 33% in one of the subjects")
# elif(sub1+sub2+sub3)/3 <40:
#     print("you are fail due to total percentage less than 40")
# else:
#     print("congratulations! You passed the exam")    
    
# A spam comment is definded as a text containing following keywords:    
# text = input("Enter the text\n")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True 
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not a spam")    

# Write a program to find whether a given username contains less than 10 characters or not.
# username = input("Enter your name\n")

# if(len(username)<10):
#     print("it contain less than 10 characters ")
# else:
#     print("it contain greater than 10 characters")    

# Write a program to find out whether a given name is present in a list or not.
# names = ["yashi", "vinu","vidhi","yashasvi","yashu"]
# name = input("Enter your name")

# if name in names:
#     print("your name is present in a list")
# else:
#     print("your name is not present in a list")    

# Write a program to calculate the grade of a student from this his marks from the following scheme.
# marks = int(input("enter your marks\n"))

# if marks>=90:
#     grade = "Ex"

# elif marks>=80:
#     grade = "A"  
# elif marks>=70:
#     grade = "B"  
# elif marks>=60:
#     grade = "C"              
# elif marks>=50:
#     grade = "D"  
# else:
#     grade = "F"

# print("your grade is" + grade)

# Write a program to find out whether a given post is talking about "harry" or not.
related = ("harry is a good boy")
post = input("enter your post\n")

if post in related:
    print("your post is talking about harry")

else:
    print("your post is not talking about harry")

