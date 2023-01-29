#Ask user for their name-------->
name = input("What's your name? ")
#Say hello to user
print("hello,", name)
print("hello,"+ name)

print("hello,", end="????") #sep="???"
print(name)

print('hello, "friends"')
print("hello, \"friends\"")

#Formet String------->
print(f"hello,{name}")


name = input("What's your name? ").strip().title()

#Remove White space from str-------->
name = name.strip()

#Capitalize user's name------->
name = name.capitalize()   # its just capitalize the first letter of first word.
name = name.title()    #it's capitalize first letter of each of the word.

#Remove White space from str and Capitalize user's name------>
name = name.strip().title()

#Formet String------->
print(f"hello, {name}")

#Combining all the strings--------->
name = input("What's your name? ").strip().title()

print("hello, ",name)

#Split user's name into first and last name-------->
first, last = name.split(" ")

print(f"hello, {first} {last}")