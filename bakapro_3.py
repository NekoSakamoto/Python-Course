# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print (list1)
# tuple1= '1,2,3', 'halalugha', 'Baka', 'not your type'
# print (tuple1)
# dict1= {"name": "Doraemon Bin AndrewTate", "age": 10, "human":False, "CETSOP":True, "Covid-19":True, "Deadly":True}
# ignore the code above
# today's topic is string. a string is just a data type like integer boolean and e.t.c. 
# a = "Talha"
# what if "Talha" is not written in double quote but sinlge or three quotes?
# b = 'Talha'
# c = '''Talha'''
# print (a, b, c)
# print (type(a))
# print (type(b))
# print (type(c))
# even after being written in single or three quotes the result is same.
# but then why should be single double or three quotes should be used, why cant i use only one? well the reason is simple and logical:
# a = "Talha's" # you can use single quote in double quote but you cant use single quote in single quote like this:
# b = 'Talha's' if i print it it will give error because for python the string ends at 'Talha' simple right?
# but then how to solve the problem? do this: a = 'Talha"s' no errors!
# but what if you want to print double quote in double quote or single quote? do this:
# a = '''Harry"s'''
# print (a) # no errors and double quote printed successfully!

# now lets talk about string slicing 
# name = "Talha"
# greetings = "Good Morning, "
# print (greetings + name) you can also do this:
# c = greetings + name it will give the same result as above
# this is string index:
#   Talha
#   ^^^^^   
#   01234
# now lets see index slicing 
name= "Talha"
# print(name[0]) # it'll print T because in index 0 is T, index starts with 0 and T is avaliable on 0 and a on 1 and l on 2
# name[0]= "ga" remember you can access a string index but cant change it.. 
# print (name[0:5])  remember it will print Talha and if [0:4] is printed it will print Talh 
# print (name[1:]) now if we type [1:] and leave space after 1 it'll print 'alha' because of the index
# a = "Doraemon Bin AndrewTate"
# slicing with skip value
# print (a[-25:-10]) it will print Doreamon Bin
# d = name[0:5:2] # from 0 (T) to 5 (a) skip every two characters, Tla will be printed
# print (d)
# String functions
# story = "Once there was a idiot named Talha who daily skipped school and made his parents sad and worry."
# print (len(story)) len function is used to check length or number of words in a string
# print (story.endswith("and worry"))  .endswith funtion is used to check if a string is ending with something as shown
# print (story.count("e")) .count function is used to see how times a letter or a word has been used in a string 
# print (story.capitalize()) .capitalize function is used to capitalize the first letter of the string in this case its O
# print (story.find("sad")) .find function is used to find a string, it will mention its string index number 
# print (story.replace("Talha", "Baka")) .replace function is used to replace a word or a letter in a string

# escape sequence characters 
# quality= "Tg has no quality\nplus he's very lazy"
# print(quality) \n is escape sequence character and if used it leaves a line and following will be printed:
# Tg has no quality
# plus he's very lazy
# following are the escape sequence characters
# quality1= "Tg has no quality\nplus he's very lazy"
# quality2= "Tg has no quality\tplus he's very lazy"
# quality3= "Tg has no quality\'plus he's very lazy"
# quality4= "Tg has no quality\\plus he's very lazy"
# print(quality1, quality2, quality3, quality4)

# practice set 
# username= input("Please enter your name:\n")
# greetings= "Good Afternoon, "
# print (greetings + username)

# letter = '''Dear <|Name|>,
# you are selected! 

# Date:'''
# n1= input("Enter your name:\n")
# n2 = input("Enter date:\n")
# letter = letter.replace("<|Name|>", n1)
# letter = letter.replace("Date:", n2)
# print (letter)
 
# n1= input("Enter Something and our program will detect if it have double spaces or not:\n")
# print(n1.find("  "))

# story= "I swear to god you're not my  lord."
# print(story.find("  "))

# letter= "Dear Talha, This python course is nice. Thanks!"
# letter= letter.replace("Dear Harry, ", "Dear Talha, \n\t")
# letter= letter.replace("nice. ", "nice.\n")
# print (letter)

# THE END