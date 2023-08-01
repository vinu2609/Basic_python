# Write a program to read the text from a given fie 'poems txt' and find out whether it contains the word 'twinkle'
# f = open('poems.txt', 'r')
# data =f.read()
# if 'Twinkle' in data:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")    
# f.close()

# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hiscore.txt' which is either blanks or contains the previous Hiscore, You need to write a program to update the Hiscore whenever game() breaks the hiscore.
# def game():
#     return 64

# score = game()
# with open("hiscore.txt") as f:
#     hiscore = int(f.read())

# if hiscore<score:
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))
    
# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13year old.
# for i in range(2,21):
#     with open(f"tables/Multiplication_table of_{i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}\n")

# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with #### by updating the same file.
# with open("sample.txt","r") as f:
#     content = f.read()

# content = content.replace("donkey","$%^@$^%#")

# with open("sample.txt","w") as f:
#      f.write(content)

# Repeat program 4 for a list of such words to be censored.
# words = ["donkey", "pagal", "kaddu"]
# with open("sample.txt","r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word,"$%^@$^%#")

#     with open("sample.txt","w") as f:
#      f.write(content)

# Write a program to mine a log file and find out whether it contains "python"
# with open("log.txt","r") as f:
#     content = f.read()

# if 'python' in content:
#     print("Yes python is present")
# else:
#     print("No python is not present")        

# Write a program to find out the line number where python is present from question 6.
# Content = True
# i = 1
# with open("log.txt") as f:
#     while Content:

#         Content = f.readline()

#         if 'python' in Content:
#             print(Content)
#             print("Yes python is present")
#             print(i)
#         i+=1    

# Write a program to make a copy of a txt file "this.txt"
# with open("this.txt","r") as f:
#     content = f.read()

# with open("copy.txt","w") as f:
#     f.write(content)   

# Write a program to find out whether a file is idential & matches the content of another file.
# file1 = "copy.txt"
# file2 = "sample.txt"

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()

# if f1 ==f2:
#     print("Files are identical")

# else:
#     print("Files are not identical")

# Write a program to wipe out the contents of a file using python.
# filename = "sample.txt"
# with open(filename,"w") as f:
#     f.write("")

# Write a python program to rename a file to "renamed_by_python.txt"
# import os

# oldname = "sample2.txt"
# newname = "renamed_by_python.txt"

# with open(oldname) as f:
#     content = f.read()

# with open(newname,"w") as f:
#     f.write(content) 

# os.remove(oldname)       






            
        
