import re
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        one = int(match.group(1))
        two = int(match.group(2))
        three = int(match.group(3))
        four = int(match.group(4))
        if one <= 255 and two <= 255 and three <= 255 and four <= 255 :
            return True
        else :
            return False
    else :
        return False
  # """ if re.search(r"^[0-9]+\.[0-9]+\.[0-9]\.[0-9]+$", ip):
     #   list_of_numbers = ip.split(".")
     #      if not int(number) in range(0, 255):
       #         return False
      #  return True
  #  else:
   #     return False"""


if __name__ == "__main__":
    main()