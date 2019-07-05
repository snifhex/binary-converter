#!/usr/bin/python
#Author - Sachin Tripathi

print"============================================================"
print "\t\t      Binary Converter"
print"\t0110100001100101011011000110110001101111"
print"============================================================"


def dec2bin(decimal):
    decimal = int(decimal)

    result = ''
    while decimal > 0:
        binary = decimal % 2
        result += str(binary)
        decimal = decimal//2

    return result[::-1]


def bin2dec(binary):
    userInput = reversed(str(binary))

    result = 0
    for i, num in enumerate(userInput):
        power = 2**i
        if int(num) == 1:
            result += power
        else:
            result += 0

    return result


def caseSwitcher(param):
    case, arguments = param.split()
    if case == "dec":
        result = dec2bin(arguments)
        return result
    elif case == 'bin':
        result = bin2dec(arguments)
        return result
    else:
        return 'Not configured case'


def main():
    userInput = input()
    answer = caseSwitcher(userInput)
    print(answer)


if __name__ == "__main__":
    main()

