myDict = {
    "fast": "In a Quick Manner",
    "harry":"A Coder",
    "marks": [1,2,3],
    "anotherdict":{'harry':'player'},
    1 : 2,
    }

# Dictionary Methods.

print(list(myDict.keys())) #Prints the keys of the dictionary.
print(myDict.values()) #Prints the keys of the dictionary. 
print(myDict.items()) #Prints the (keys, values) for all contents of the dictionary. 
print(myDict)
updateDict = {
    "Vini":"Friend",
    "Aarchi":"Friend"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict. 
print(myDict)



print(myDict.get("harry")) # Prints value associated with key "harry".
print(myDict["harry"]) # Prints value associated with key "harry".

# The difference between .get & [] syntax in dictionaries.
print(myDict.get("harry2")) # returns none as harry2 is not present in the dictionary.
print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary.






