#normally---------->
x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#invent a function that determine if the number is even------>
def main():
    x = int(input("What is x? "))
    if is_even(x):   #function as boollean expression
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:  #using Boolen Expression
        return True
    else:
        return False

main()

#more pythonic------->
def main():
    x = int(input("What is x? "))
    if is_even(x):   #function as boollean expression
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

#returing the question it self--------->
def main():
    x = int(input("What is x? "))
    if is_even(x):   #function as boollean expression
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()