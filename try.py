#!/usr/bin/python2.7
import csv
import sys

def sum (array):
    suma = 0
    while array != 0:
        suma += array%10
        array = array/10
    return suma

def collatz(number):
    contor = 0
    while number > 1:
        contor += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    return contor

def parsecsv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for elem in row:
                if elem.isdigit():
                    if int(elem) >= 100:
                       print elem + '#Collatz este: ',
                       print collatz(int(elem))
                    elif int(elem) > 10 and int(elem) < 100:
                       print elem + '#Suma cifrelor este: ',
                       print sum(int(elem))
                    else:
                       print '### 7 la puterea ' + elem,
                       print pow(7, int(elem))

def parsecsv1(file, file2):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for elem in row:
                file2.write(elem)
                file2.write('\n')
                #print "%s\t%s" % (elem, 1)
    file2.close()
if __name__ == "__main__":
    abcd = open('/home/flavius/Desktop/input.txt', 'w')
    parsecsv1("/home/flavius/PDIII/thads2011.csv", abcd)
