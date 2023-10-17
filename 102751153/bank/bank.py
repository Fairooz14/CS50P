greet = input("Greeting: ")
#lower foe cae-insensitiveness.
if "hello" in greet.lower().strip():
    print("$0")
elif greet.strip()[0] == "H" or greet.strip()[0] == "h":
    print("$20")
else:
    print("$100")
