#Checking every condition one by by and printing the correct one----------->
x = int(input("What si x? "))
y = int(input("What is y? "))

#"if x < y:" this format call bullien formet after":" 4 space is necessary as it indicates "?"-------->
if x < y:
    print("X is less than Y")
if x > y:
    print("X is greater than Y")
if x == y:
    print("X is equal to Y")

#Only checking 1 or 2. should not go through every condition----------->
x = int(input("What si x? "))
y = int(input("What is y? "))

#"if x < y:" this format call boolean expression after":" 4 space is necessary as it indicates "?"---------->
if x < y:
    print("X is less than Y")
elif x > y:
    print("X is greater than Y")
else:
    print("X is equal to Y")

#Use of OR------------------------>
x = int(input("What si x? "))
y = int(input("What is y? "))

if x < y or x > y:
    print("X is not equal to y")
else:
    print("X is equal to y")
