#Reading CSV-file to list of lists.
import csv
exampleFile = open('Badprice.csv', 'rU')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


#Declaration of variables.
maxValue = 0
minValue = 0
maxIndex = ''
minIndex = ''
avgPrice = 0
avgSquareFootage = 0
countPrice = 0
countSquareFootage = 0


#Creation of two lists.
for row in exampleData:
    if row[9].isalpha():
        continue
    else:
        if float(row[9]) > 0 and float(row[6]) > 0:
            avgPrice += float(row[9])
            avgSquareFootage += float(row[6])
            countPrice += 1
            countSquareFootage += 1
            if (maxValue < float(row[9])):
                 maxValue = float(row[9])
                 maxIndex = row[0]
            if (minValue > float(row[9])):
                 minValue = float(row[9])
                 minIndex = row[0]


#Printing results.
for row in exampleData:
    if (row[0] == maxIndex):
        print('Max price of real estate -- ' + str(row) + ' is: ' + str(maxValue) + '$.')
    if (row[0] == minValue):
        print('Min price of real estate -- ' + str(row) + ' is: ' + str(minValue) + '$.')

print('Average square footage is -- ' + str(avgSquareFootage / countSquareFootage))
print('Average price is -- $' + str(avgPrice / countPrice))