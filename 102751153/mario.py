#vertical barier--------->
for _ in range(3):
    print("#")

#Defining the print--------->
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
       print("#")

main()

#Another way to print------->
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height , end="")

main()

#horizontal barier-------->
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

#Wall barier----->
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):

            #Print brick
            print("#" , end="")
        print()

main()

#An alternative----->
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        print("#" * size)

main()