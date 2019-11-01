classic = {'C': 1972, 'Java': 1995, 'Python': 1991}
modern = {'Kotlin': 2011, 'Rust': 2010, 'Swift': 2014}

print(classic)
print(modern)

classic.update(modern)

print("\nCombination")
print(classic)

delKey = input("\nEnter a key to remove- ")
returnVal = classic.pop(delKey, None)
if returnVal == None:
     print("Key not found")
print("\nUpdate")
print(classic)