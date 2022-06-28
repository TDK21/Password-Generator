# This is my first password generator, there could be a lot of bugs, etc.
# Author: TDK21

import random
wSigns = ['!', '.', ',', '@', '-', '_', '+', '=', '$', '%']
nSigns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():

    print("Hello! This app generates random password")
    print()
    print("How many symbols do you need?")
    symbols = int(input())
    print("Do you need special sign? [y/n]")
    signs = input()
    passwd = generatePassword(symbols, signs)
    print("Here your new password: ", passwd)


def generatePassword(symbols, signs):
    pwd = ""
    i = 0
    j = 0
    letterBefore = ""
    numberOfSpecialSymbols = symbols // 5
    while i != symbols:
        if signs == "y":
            typeSymbol = random.randint(0, 1)
            if typeSymbol == 0:
                letter = random.choice(nSigns)
            if typeSymbol == 1 and j != numberOfSpecialSymbols:
                letter = random.choice(wSigns)
                j += 1
        else:
            letter = random.choice(nSigns)
        if letter != letterBefore:
            pwd = pwd + letter
        else:
            i -= 1
        i += 1
        letterBefore = letter
    return pwd

if __name__ == "__main__":
    main()