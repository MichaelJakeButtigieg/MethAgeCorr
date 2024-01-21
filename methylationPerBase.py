import csv
from SeparateNames import *
from writeToCSV import *

filepath = ''
datamatrix = []
# LOGIC OF PROGRAM
# Load file in
# Iterate over each chromosome location and get the bp length
# Divide each methylation value by the bp length of the chromosome locations
# Write it out to a table which you can print into file
# make it a method you can extract

def methylationPerBase_F(filepath):

    final = []
    temporary = []

    with open(filepath, 'r') as file:
        data = csv.reader(file)

        for row in data:
            hold = row
            length = len(row)
            sthold = str(hold[0])
            separated = sthold.split("_")
            # separated.insert(3, "BS")
            if separated[0] > '':
                try:
                    perBase = int(separated[-1]) - int(separated[1])
                # print(row)
                except ValueError:
                    pass

                for i in range(1,length):
                    try:
                        perBaseMeth = (float(row[i])/perBase)
                        row[i] = perBaseMeth

                    except ValueError:
                        pass


                hold = row
            final.append(hold)
        # print(final)
    writeToCSV(final)
    return (final)

def methylationPerBase(datamatrix):

    final = []
    temporary = []
    perBase = 0
    # perBaseMeth = 0.000

    for row in datamatrix:
        hold = row
        length = len(row)
        sthold = str(hold[2])
        separated = sthold.split("_")
        # separated.insert(3, "BS")
        if separated[0] > '':
            try:
                perBase = int(separated[-1]) - int(separated[1])
            # print(row)
            except ValueError:
                pass

            for i in range(2,length):
                try:
                    perBaseMeth = (float(row[i])/perBase)
                    row[i] = perBaseMeth

                except ValueError:
                    pass


            hold = row
        final.append(hold)
    # print(final)
    return (final)

