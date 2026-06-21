import func
import time
import os
# for each in func.code:
#     print(each, func.code[each])
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    what = input("Do you want to encode or decode (or quit)? ").lower()
    if what == "encode":
        to_encode = input("What to encode? ")
        encoded = ""
        to_decode = ""



        for char in range(len(to_encode)):
            if to_encode[char] in func.code:
                encoded = encoded + func.code[to_encode[char]]
            else:
                print("Error")

        print("Encoded string:", encoded, "<-- copy it")
        time.sleep(5)
        clear_console()
    elif what == "decode":
        encoded = input("What to decode? ")
        to_decode = ""
        for char in range(0, int(len(encoded)), 2):
            if encoded[char:char+2] in func.decode:
                to_decode = to_decode + func.decode[encoded[char:char+2]]
            else:
                print("Error")

        print("Decoded string:", to_decode, "<-- copy it")
        time.sleep(5)
        clear_console()
    elif what == "quit":
        quit()
    else:
        print("Dont troll me...")