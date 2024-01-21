import csv
from writeToCSV import *

filepath = '/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/Hovarth_ UniqueID _ChrLoc.csv'

def combineNamesInFile(filepath):
    with open(filepath) as file:
        try:
            regions = csv.reader(file)
            # contains the chromosomes and chromsome ranges (i.e. start and end locations) that we are looking for in the experimental data
        except:
            print("File Not Found, Please check your file path")

        idandchr = []
        full_chr = []
        count = 0
        idchrheader = ['CG_Identifier', 'Chr_Loc']

        for row in regions:
            if count == 0:
                count += 1
            else:
                temp = 'chr' + row[1] + '_' + row[2] + '_' + row[3]
                full_chr.append(row[0])
                full_chr.append(temp)
                full_chr = []
                idandchr.append(full_chr)
    print(idandchr)
    writeWHeader(idandchr, idchrheader)

combineNamesInFile(filepath)