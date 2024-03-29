from bank import value
def main():
    test_return_zero()
    test_return_20()
    test_return_100()

def test_return_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('Hello Gi') == 0
def test_return_20():
    assert value('Hi') == 20
    assert value('Hey') == 20
def test_return_100():
    assert value('Good moring') == 100
    assert value('Whats up') == 100
    assert value('Yo') == 100

if __name__ == "__main__":
    main()