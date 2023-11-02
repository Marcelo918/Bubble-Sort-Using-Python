'''
# ******************************************************************************
# *                               COPYRIGHT NOTICE                             *
# ******************************************************************************
# *                                                                            *
# *  This code is authored by Marcelo Villalobos Diaz                          *
# *  You are free to use, modify, and distribute this code, provided           *
# *  you give appropriate credit by including the author's name.               *
# *                                                                            *
# *  Copyright (c) 2023 Marcelo Villalobos Diaz                                *
# *                                                                            *
# ******************************************************************************
'''

'''
Description - The code below does the following:

             A. Writes 50 to 55 random numbers (between 0 - 100) to a text file
             B. Opens the file and reads the numbers from it into a list
             C. Sorts the list using bubble sort and shows it
             D. Calculates the median 
'''

import random

mySecondFile = open("somefile.txt", 'w')

X = random.randint(50, 55)

for i in range(0, X, 1):
    Y = random.randint(0, 100)
    mySecondFile.write(str(Y))
    if i != X-1:
        mySecondFile.write('\n')
mySecondFile.close()

myFile = open("somefile.txt", 'r')
listSecondFile = myFile.read().split('\n')
myFile.close()

print("Unsorted List of %i Random Numbers: \n" % X)
print(listSecondFile)
print(" ")

listSecondFile = [int(x) for x in listSecondFile]


def bubble(list_a):
    indexing_length = len(list_a)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print("Sorted List of the %i Random Numbers: \n" % X)
SortedList = bubble(listSecondFile)
print(SortedList)
print(" ")

if len(SortedList) % 2 != 0:
    medianIndex = int(len(SortedList)/2)
    median1 = SortedList[medianIndex]
    print('median1 =', median1)
elif len(SortedList) % 2 == 0:
    medianIndex1 = int(len(SortedList)/2)
    medianIndex2 = int(len(SortedList)/2) - 1
    median2 = (SortedList[medianIndex1] + SortedList[medianIndex2])/2
    print('median2 =', median2)
