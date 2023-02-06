#def TO DEFINE SOMETHING  THROUGH A FUNCTION----------->
def hello():
    print("hello")

name = input("What si name? ")
hello()
print(name)

#Using parameter inside the function------------->
def hello(to):
    print("hello, ",to)

name = input("What is your name ? ")
hello(name)
#Assigning a defult output to the paremeter of the defined function----------->
def hello(to="world"):
    print("hello, ",to)

hello()  #without an argument.(using the defult output)
name = input("What is your name? ")
hello(name)

#Use of main function by calling it---------->
def main():
    name = input("what is your name ? ")
    hello(name)

def hello(to="world"):
    print("hello, ",to)

main()