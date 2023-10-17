#returning a value to the main function------->
def main():
    x =int(input("What si x? "))
    print("X squared is ", square(x))

def square(n):
    return n*n #n**2 or pow(n,2)
main()