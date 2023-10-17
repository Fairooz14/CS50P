#[WORKING WITH INTEGER ADDITION]===========>>>>
#assiging value directly------->
x = 1
y = 2


z = x + y
print(z)

#print the value together (contrating strings)--------->
x = input("what is x? ")
y = input("what is y? ")

z = x + y
print(z)

#Taking Input------------->
x = input("what is x? ")
y = input("what is y? ")

z = int(x) + int(y)
print(z)

#making it shorter-------------------->
x = int(input("What is X? "))
y = int(input("What si y? "))

z = x + y
print(z)

#one line addition--------------------->
print(int(input("What is X? ")) + int(input("What is Y? ")))


#WORKING WITH FRACTION ADDITION----------------->
x = float(input("What is X? "))
y = float(input("What si y? "))

print(x + y)

#round(nnumberumber[, ndigits])----------------------->
x = float(input("What is X? "))
y = float(input("What si y? "))

z = round(x + y)
print(z)
#using comma(",") in a number--------------->
print(f"{z:,}")

#[WORKING WITH FRACTION DIVISION]============>>
x = float(input("What is X? "))
y = float(input("What si y? "))

print(x / y)
#spacifiying the limit after point------------>
x = float(input("What is X? "))
y = float(input("What si y? "))

z = round(x / y, 2)
print(z)
print(f"{z:.2f}")   ### using format string