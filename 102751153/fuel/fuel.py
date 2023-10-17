def main():
    value = get_inp('Fraction: ')
    if value <= 0.01:
        print('E')
    elif value >= 0.99:
        print('F')
    else:
        print(f'{value:.0%}')

def get_inp(prompt):
    while True:
        try:
            x = input(prompt)
            split = x.split('/')
            lst = []
            for num in split:
                lst.append(int(num))
            if lst[0] > lst[1]:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            p = lst[0] / lst[1]
            return p


main()