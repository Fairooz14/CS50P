#ask = input("Input: ")
#print ("Output: ", end="")

#for char in ask :
#    if not char.lower() in ['a' , 'e', 'i', 'o', 'u']:
#       print(char,end="")

#print()
def main():
    msg = input("Input: ")
    msg_without_vowels = shorten(msg)
    print("Output: " + msg_without_vowels)
def shorten(word):
    word_without_vowels = ""
    for char in word :
        if not char.lower() in ['a' , 'e', 'i', 'o', 'u']:
            word_without_vowels += char
    return word_without_vowels

if __name__ == "__main__":
    main()