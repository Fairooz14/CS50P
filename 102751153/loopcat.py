#Rendom Repeatation---------->
print("meow")
print("meow")
print("meow")

#using {WHILE}. It works as a boolean expression---------->
i = 3
while i != 0:
    print("meow")
    i = i - 1
#Another way of using while condition--------->
i = 0     #[INISIALIZATION]
while i < 3:     #[CONDITION]
    print("meow")
    i = i + 1 #OR "i += 1" BUT python doesn't have i++ or i-- or --i or ++i tendency  [INCREMENT OR DECREMENT]

#using "list" of things in a loop is {FOR} loop-------->
for i in [0, 1, 2]:  # Here "[0, 1, 2]" is the list
    print("meow")

#using unlimited-------->
for i in range(3):   # the variable can be shown is this way "for _ in range(3): "
    print("meow")

#Being more pythonic way-------->
print("meow" * 3)
print("meow\n" * 3)
print("meow\n" * 3 , end="")

#Asking for input using while loop and run it input a for loop--------->
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#let's make a MEOW function--------->
def main():
    meow(3)  #setting the value defult

def meow(n):
    for _ in range(n):
        print("meow")

main()

#Asking for input but this time need to return a value to the meow function for printing-------->
def main():
    number = get_number()
    meow(n)  # "meow(n)" or "meow(number)" both could be used

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break  # after getting out of the loop it needs to hand back the value of a function (retun is used outside of the loop but inside of the function)
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()