# Code funtions done by: Maria Atef Edward 
# main menu done: by Abraam Morcos

# problem 1 function
# this function converts from decimal to binary
def dec_to_binary(n):
    binInp = ""
    while n > 0:
        remainder = n % 2
        binInp = str(remainder) + binInp
        n //= 2
    return binInp


# this function converts from decimal to octal
def dec_to_octal(n):
    octInp = ""
    while n > 0:
        remainder = n % 8
        octInp = str(remainder) + octInp
        n //= 8
    return octInp


# this function converts from decimal to hexadecimal
def dec_to_hex(n):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""
    while n > 0:
        remainder = n % 16
        hex_string = hex_digits[remainder] + hex_string
        n //= 16
    return hex_string


# this function converts from octal to decimal
def octal_to_dec(n):
    oct_num = int(n)
    dec = 0
    power = 0
    while oct_num > 0:
        digit = oct_num % 10
        dec = dec + digit * (8 ** power)
        oct_num = oct_num // 10
        power = power + 1
    return dec


# this function converts from octal to binary
def octal_to_bin(n):
    oct_num = int(n)
    binary_num = 0
    power = 0
    while oct_num > 0:
        digit = oct_num % 2
        binary_num += digit * (10 ** power)
        oct_num = oct_num // 2
        power += 1
    return binary_num


# this function converts from octal to hexadecimal
def octal_to_hexa(n):
    octal_num = int(n)
    hex_num = 0
    power = 0
    while octal_num > 0:
        digit = octal_num % 16
        hex_num += digit * (10 ** power)
        octal_num = octal_num // 16
        power += 1
    return hex_num


# this function converts from hexadecimal to decimal
def hexa_to_dec(b):
    val = 0
    for x in range(len(b)):
        d = b[-1] if b \
            else None
        if d == "A":
            d = 10
        elif d == "B":
            d = 11
        elif d == "C":
            d = 12
        elif d == "D":
            d = 13
        elif d == "E":
            d = 14
        elif d == "F":
            d = 15

        e = pow(16, x)
        f = e * int(d)
        val += f

        b = b[:-1]
    return val


# this function converts from hexadecimal to binary
def hexa_to_binary(n):
    binary = ""
    for x in range(len(n)):
        x = n[-1] if n else None
        if x == "0":
            binary = "0000" + binary
        elif x == "1":
            binary = "0001" + binary
        elif x == "2":
            binary = "0010" + binary
        elif x == "3":
            binary = "0011" + binary
        elif x == "4":
            binary = "0100" + binary
        elif x == "5":
            binary = "0101" + binary
        elif x == "6":
            binary = "0110" + binary
        elif x == "7":
            binary = "0111" + binary
        elif x == "8":
            binary = "1000" + binary
        elif x == "9":
            binary = "1001" + binary
        elif x == "A" or x == "a":
            binary = "1010" + binary
        elif x == "B" or x == "b":
            binary = "1011" + binary
        elif x == "C" or x == "c":
            binary = "1100" + binary
        elif x == "D" or x == "d":
            binary = "1101" + binary
        elif x == "E" or x == "e":
            binary = "1110" + binary
        elif x == "F" or x == "f":
            binary = "1111" + binary
        n = n[:-1]
    return binary


# this function converts from hexadecimal to octal
def hexa_to_octal(n):
    binary = ""

    for i in range(len(n)):
        x = n[i]
        if x == "0":
            binary += "000"
        elif x == "1":
            binary += "001"
        elif x == "2":
            binary += "010"
        elif x == "3":
            binary += "011"
        elif x == "4":
            binary += "100"
        elif x == "5":
            binary += "101"
        elif x == "6":
            binary += "110"
        elif x == "7":
            binary += "111"
        elif x == "8":
            binary += "1000"
        elif x == "9":
            binary += "1001"
        elif x == "A" or x == "a":
            binary += "1010"
        elif x == "B" or x == "b":
            binary += "1011"
        elif x == "C" or x == "c":
            binary += "1100"
        elif x == "D" or x == "d":
            binary += "1101"
        elif x == "E" or x == "e":
            binary += "1110"
        elif x == "F" or x == "f":
            binary += "1111"

    while len(binary) % 3 != 0:
        binary = "0" + binary

    octal = ""
    i = 0
    while i < len(binary):
        decimal_value = 0
        for j in range(3):
            decimal_value = (decimal_value << 1) | int(binary[i + j])
        octal += str(decimal_value)
        i += 3
    octal = str(int(octal))
    return octal


# this function converts from binary to decimal
def binary_to_dec(binary):
    b = list(str(binary))
    val = 0
    for x in range(len(b)):
        d = b[-1] \
            if b \
            else None
        if d == "1":
            val = val + pow(2, int(x))
    return val


# this function converts from binary to octal
def binary_to_octal(binary):
    octal = ''
    binary = "0" * (3 - (len(binary) % 3)) + binary
    for i in range(0, len(binary), 3):
        bits = binary[i:i + 3]
        val = 0
        for j in range(len(bits)):
            val = val * 2 + int(bits[j])
        octal += str(val)
    return octal


# this function converts from binary to hexa
def binary_to_hexa(binary):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""
    binary = "0" * (4 - (len(binary) % 4)) + binary
    for i in range(0, len(binary), 4):
        group4 = binary[i:i + 4]
        decimal_value = int(group4, 2)
        hex_digit = hex_digits[decimal_value]
        hex_string += hex_digit
    return hex_string

# problem 1 menus
def menu1():# menu1 used for inputing and validating the user's choice whether its A or B only
    while True:
        choice = input("A- Insert a new number\nB- Exit Program\nPlease choose: ")
        if choice.upper() == "A":
            num = input("Insert a number: ")
            menu2(choice,num)
            return True, num
        elif choice.upper() == "B":
            print("Exiting")
            exit()
            return False, None
        else:
            print("Invalid choice. Please enter A or B.")
            return True, None


def menu2(choice,num):#menu1 used for inputing and validating the user's choice whether its A or B or C or D
    # it is also used for validating the input of the user and whether it matches his choice
    while True:
        # menu 2
        print("Please enter the base you want to change from: ")
        choice2 = input("A-Decimal\nB-Binary\nC-Octal\nD-Hexadecimal").upper()

        if choice2 == 'A':
            base = 10
            valid_dictionary = "0123456789ABCDEFabcdef"
            for digit in str(num):
                if digit not in valid_dictionary[:int(base)]:
                    print('ERROR not valid base')
                    menu1()
            else:
                menu3(choice2, num, base)
                break
        elif choice2 == 'B':
            base = 2
            valid_dictionary = "0123456789ABCDEFabcdef"
            for digit in str(num):
                if digit not in valid_dictionary[:int(base)]:
                    print('ERROR not valid base')
                    menu1()
            else:
                menu3(choice2, num, base)
                break
        elif choice2 == 'C':
            base = 8
            valid_dictionary = "0123456789ABCDEFabcdef"
            for digit in str(num):
                if digit not in valid_dictionary[:int(base)]:
                    print('ERROR not valid base')
                    menu1()
            else:
                menu3(choice2, num, base)
                break
        elif choice2 == 'D':
            base = 16
            valid_dictionary = "0123456789ABCDEFabcdef"
            for digit in str(num):
                if digit not in valid_dictionary[:int(base)]:
                    print('ERROR not valid base')
                    menu1()
                else:
                    menu3(choice2, num, base)
                    break
        else:
            print("Please enter a valid choice: ")

# menu 3
def menu3 (choice2,num,base):#menu1 used for inputing and validating the user's choice whether its A or B or C or D
    #it is also used to convert numbers from chosen base to other chosen base
    while True:

        print("Please enter the base you want to change to: ")
        choice3 = input("A-Decimal\nB-Binary\nC-Octal\nD-Hexadecimal")

        if choice3.upper() in ["A", "B", "C", "D"]:
            break
        else:
            print("Please enter a valid choice: ")


    if choice2.upper() == "A" and choice3.upper() == "B":
        num = str(dec_to_binary(int(num)))
        print(num)
        menu1()
    elif choice2.upper() == "A" and choice3.upper() == "A":
        print(num)
    elif choice2.upper() == "A" and choice3.upper() == "C":
        num = str(dec_to_octal(int(num)))
        print(num)
        menu1()
    elif choice2.upper() == "A" and choice3.upper() == "D":
        num = str(dec_to_hex(int(num)))
        print(num)
        menu1()
    elif choice2.upper() == "B" and choice3.upper() == "A":
        num = str(binary_to_dec(num))
        print(num)
        menu1()
    elif choice2.upper() == "B" and choice3.upper() == "B":
        print(num)
        menu1()
    elif choice2.upper() == "B" and choice3.upper() == "C":
        num = str(binary_to_octal(num))
        print(num)
        menu1()
    elif choice2.upper() == "B" and choice3.upper() == "D":
        num = str(binary_to_hexa(num))
        print(num)
        menu1()
    elif choice2.upper() == "C" and choice3.upper() == "A":
        num = str(octal_to_dec(num))
        print(num)
        menu1()
    elif choice2.upper() == "C" and choice3.upper() == "B":
        num = str(octal_to_bin(num))
        print(num)
        menu1()
    elif choice2.upper() == "C" and choice3.upper() == "C":
        print(num)
        menu1()
    elif choice2.upper() == "C" and choice3.upper() == "D":
        num = str(octal_to_hexa(num))
        print(num)
        menu1()
    elif choice2.upper() == "D" and choice3.upper() == "A":
        num = str(hexa_to_dec(num))
        print(num)
        menu1()
    elif choice2.upper() == "D" and choice3.upper() == "B":
        num = str(hexa_to_binary(num))
        print(num)
        menu1()
    elif choice2.upper() == "D" and choice3.upper() == "C":
        num = str(hexa_to_octal(num))
        print(num)
        menu1()
    elif choice2.upper() == "D" and choice3.upper() == "D":
        print(num)
        menu1()
    else:
        print("Invalid input for the selected base.")

menu1()
