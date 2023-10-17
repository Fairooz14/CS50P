equation = input("Expression: ")
x, y, z = equation.split(" ")
x1 = float(x)

z1 = float(z)
if y == "+":
    sum = x1 + z1
    print(sum)
if y == "-":
    sub = x1 - z1
    print(sub)
if y == "*":
    mul = x1 * z1
    print(mul)
if y == "/":
    div = round(x1 / z1,1)
    print(div)