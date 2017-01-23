#!/usr/bin/python
#Author - Sachin Tripathi

print"============================================================"
print "\t\t      Binary Converter"
print"\t0110100001100101011011000110110001101111"
print"============================================================"
decimal = input("Enter the number you want to convert:\n>")
decimal_o = str(decimal)
b = []
while decimal > 0:
    if decimal%2 == 0:
        b.append(0)
    else:
        b.append(1)
    decimal= decimal/2
binary =(b[::-1])
print "Binary conversion for "+decimal_o+" is "+str(binary)

