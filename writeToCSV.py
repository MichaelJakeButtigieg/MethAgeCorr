import csv

toWrite = []
header = []

def writeToCSV(toWrite):

    choice = input("Do you want to input a header? (Y/N)")

    if choice == 'Y':
        headerIn = input("Enter the headers of the columns. Separate each column header with a ',' \n")
        header = headerIn.split(',')

    fileName = input("Enter the name you want to give your file: \n")

    with open(fileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(header)
        csvwriter.writerows(toWrite)

def writeWHeader(toWrite,header):
    fileName = input("Enter the name you want to give your file: \n")

    with open(fileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(toWrite)