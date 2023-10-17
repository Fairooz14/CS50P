ask = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " )
#strip to remove extra space of input------------->
if( ask.strip() == "42"):
    print("Yes")
# as the input could be incase sensitive---------------->
elif(ask.lower() == "forty-two" or ask.lower() == "forty two"):
    print("Yes")
else:
    print("No")