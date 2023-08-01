# Write a python program to display a user entered name followed by Good Afternoon using input() functions.

name = input("Enter your name")
print("Good Afternoon,"+ name)

# Write a python program to fill in a letter template given below with name and date.

letter = '''Dear <|NAME|>
Greetings from ABC coding house. I am happy to tell you about your selection
Have a great day ahead!
Thanks and regards,
bill

Date: <|DATE|>'''
name = input("Enter your name\n")
date = input("Enter date\n") 
letter = (letter.replace("<|NAME|>",name))
letter = (letter.replace("<|DATE|>",date))
print(letter)

# Write a python program to detect double spaces in a string.

st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

# Replace the double spaces from problem 3 with single spaces.

st = "This is a string with double  spaces"
st = st.replace("  "," ")
print(st)

# Write a pyhon program to format the following letter using escape sequences characters.

letter = "Dear Harry,\nThis python cource is nice.\n\tThanks!"
print(letter)









