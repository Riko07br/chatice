#by Natanael Felix
while True:
    print()
    print("digite o numero: ")
    savedNumber = int(input())

    print("binary--------------------")
    number = savedNumber
    #count chars to set spacing
    maxLenght = len(str(number))

    binarySeparated = ""

    while number > .6:
        #indent shit
        spaceAmount =  maxLenght - len(str(number))
        spaces = ""
        for s in range(0, spaceAmount):
            spaces += " "

        currentBinary = ("1" if number % 2 != 0 else "0")
        binarySeparated += currentBinary

        print(spaces + str(number) + " | " + currentBinary)   
        
        if number % 2 != 0:
            number -= 1

        number = int(number / 2)
        pass
    print()
    count = 0    
    binaryPrintable = ""

    for b in binarySeparated:
        binaryPrintable += b
        count+=1
        if count == 3:
            binaryPrintable+= " | "
            count = 0
        pass
    pass

    #print inverted shit
    print(binaryPrintable[::-1])

    print()
    print("octal--------------------")
    # found at:
    # https://www.programiz.com/python-programming/examples/conversion-binary-octal-hexadecimal
    def DecimalToOctal(n):
        if(n > 0):
            # recursively calling on n/8    
            DecimalToOctal(int(n/8))
            # printing the remainder
            print(n%8, end='')

    DecimalToOctal(savedNumber)
    
    print()
    print("ir de novo? [S/N]: ")    
    again = input()

    if(again != "S" and again != "s"):
        break