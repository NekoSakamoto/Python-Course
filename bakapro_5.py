# today's topic is dictionary and sets
# myDict= {
#     "Baka" and "baka": "Stupid (a thing or a person)",
#     "Neko" and "neko": "A cat",
#     "Kawaii" and "kawaii": "Cute (a thing or a person)",
#     "Marks" and "marks": [0,69,95],
#     "anotherdict": {'weeb':'anime lover'},
#     10: 20
# }
# n1= input("Search: ")
# print (myDict[n1])
# myDict['Marks']= [10, 70, 90]
# print (myDict['anotherdict']['weeb'])

# Dict functions
# print(myDict.keys()) prints the keys of the dictionary
# print(myDict.values()) prints the values of the dictionary
# print(myDict.items()) prints keys and values of the dictionary
# newDict= {
#     "tuskkomi": "in-depth",
#     "osananajimi": "childhood friends"
# }
# myDict.update(newDict) updates the dictionary
# print (myDict)
# print(myDict.get("baka")) prints the value of the given key from dictionary

# Sets - set is collection of non-repetitive elements
# set1= {1, 2, 3, 4, 5, 1} 
# if i add 1 again at the end of a set it will ignore it because it is repeating one more time
# print (set1) it will only print 1 2 3 4 5 not 1
# creating an empty set

# Set methods
# b = set()
# b.add (4)
# b.add (5) # you cannot add dictionary or lists to sets
# print(len(b)) or print (len(set1)) len method prints the length of a set
# b.remove(5) remove method removes an element
# print(b)
# print (b.intersection()) gives an intersection of a set
# print (b.union()) gives union of a set
# print (b.pop()) removes any number from the set
# print (b.clear()) empties the set

## Practice Set
# myDict= {
#     "Baka" and "baka": "Stupid (a thing or a person)",
#     "Neko" and "neko": "A Cat",
#     "Kawaii" and "kawaii": "Cute (a thing or a person)",
#     "Marks" and "marks": [0,69,95],
#     "anotherdict": {'weeb':'Anime lover'},
#     10: 20
# }
# n1= input("Search: ")
# print (myDict.get(n1))

# num1= int(input("Enter your number 1: "))
# num2= int(input("Enter your number 2: "))
# num3= int(input("Enter your number 3: "))
# num4= int(input("Enter your number 4: "))
# num5= int(input("Enter your number 5: "))
# num6= int(input("Enter your number 6: "))
# num7= int(input("Enter your number 7: "))
# num8= int(input("Enter your number 8: "))
# set2= {num1, num2, num3, num4, num5, num6, num7, num8}
# print(set2)

# s = {20, 20.0, "20"}
# print (len(s)) suprisingly the length will be 2 not 3 because 20 and 20.0 are equal numbers

# favLang= {}
# a = input("Enter your favourite programming language Sufyan\n")
# b = input("Enter your favourite programming language Tayyab\n")
# c = input("Enter your favourite programming language Ahmed\n")
# d = input("Enter your favourite programming language Zubair\n")
# favLang['sufyan']= a
# favLang['tayyab']= b
# favLang['ahmed']= c
# favLang['zubair']= d
# print(favLang)
