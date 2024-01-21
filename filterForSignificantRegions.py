import csv
from SeparateNames import *
from combineName import *
from writeToCSV import *
from methylationPerBase import *

experimentalData = input("Enter full file path for your experimental data: \n")
# Get file path from user for the experimental data file. Needs to be as .csv file (we can add other formats if necessary)
try:
    expData = separatenames(experimentalData)
    # print(expData)
except:
    print("File Not Found, Please check your file path")

# regionFilter = input("Enter the full file path for your region filter: \n")
regionFilter = '/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/Horvath_ID_Chr_Gene.csv'
# Get the file path from user of the regions which are filtered for in the experimental data
with open(regionFilter) as file:
    try:
        regions = csv.reader(file)
        # contains the chromosomes and chromsome ranges (i.e. start and end locations) that we are looking for in the experimental data
    except:
        print("File Not Found, Please check your file path")

    # idandchr = []
    # full_chr = []
    # count = 0
    # idchrheader = ['CG_Identifier', 'Chr_Loc']
    #
    # for row in regions:
    #     if count == 0:
    #         count += 1
    #     else:
    #         temp = 'chr' + row[1] + '_' + row[2] + '_' + row[3]
    #         full_chr.append(row[0])
    #         full_chr.append(temp)
    #         full_chr = []
    #         idandchr.append(full_chr)
    #
    # writeWHeader(idandchr, idchrheader)
    # Combines the Chr_Start_End and writes tehm into a csv file alongside their  CGxxxx identifiers


    chrgroup = []
    fullagree = []
    within = []
    other = []

    for row in regions:
        regionrow = row
        # print(regionrow)
        identifier = regionrow[0]
        chr = "chr" + str(row[1])
        # Adds "chr" in front of the chromosome number so that it is consistent with the chromosome number in 'data'
        genstart = row[2]
        # print("Hov GenS: " + genstart)
        genend = row[3]
        # print("Hov GenE: " + genend)

        if genstart > genend:
            genstart = row[3]
            genend = row[2]
            # if genestart is larger than geneend swaps them to get the compliment chr locations (because all of the chromosome locations in the 'data' file are start > end

        for row in expData:

            if str(row[0]) == chr:
                # print(row[0],chr,row[1], genstart, row[2],  genend)

                if row[1] == genstart and row[2] == genend:
                    # row.insert(0, regionrow[0])
                    # inserts cg identifier (e.g. cg00000) at the beginning of row
                    fullagree.append(row)

                    # checks if the hovarth range and the 'data' range are exactly the same, if they are adds the row (chr,start,end) to the full agree list

                elif row[1] >= genstart and genend >= row[2]:
                    # checks if the 'data' range is within the hovarth range (row[1] = start loc, row[2] = endloc
                    # print(row[1])
                    check = int(row[1]) - int(genstart)
                    check2 = int(genend) - int(row[2])

                    if check > 0 and check2 > 0:
                        # checks if the 'data' range is within the hovarth range (row[1] = start loc, row[2] = endloc
                        placeholder = []
                        cgID = regionrow[0]
                        geneID = regionrow[-1]
                        chri = row[0]
                        chrstart = row[1]
                        chrend = row[2]
                        chrloc = chr + "_" + chrstart + "_" + chrend
                        placeholder.insert(0, cgID)
                        placeholder.insert(1, geneID)
                        placeholder.insert(2, chrloc)
                        # placeholder.insert(1, chri)
                        # placeholder.insert(2, chrstart)
                        # placeholder.insert(3, chrend)
                        # print(placeholder)
                        within.append(placeholder)
                        # print(placeholder)
                        placeholder = []



                    else:
                            # printOther = input("Would you like to print out a file with the non-significant regions? (T/F) \n")
                        # if printOther == "T":
                        pass

# writeToCSV(within)
# Gives a csv file with the separated significant chr locations (chr, start, end) and the CpG Id (i.e. cgxxxx)
# significantRegions = combineNames(within)
significantRegions = within

locationdata = []
sigRegionFilter = []
methylationdata = []
finalheader = []
identifier = []

counter = 0
counter2 = 0


# identifiers = combineNamesFile(regionFilter)

# for z in identifiers:
#     if counter2 == 0:
#         counter2 += 1
#     else:
#         temp = 'chr' + z
#         identifier.append(temp)
#         print(z)



with open(experimentalData, 'r') as file:
    # Set filepath as the first provided file path
    expDataset = csv.reader(file)

    # for row in significantRegions:
    #     sigRegionFilter.append(row)
    #     # print(sigRegionFilter)

    for row in expDataset:
        if counter == 0:
            for i in range(0,len(row)):
                finalheader.append(row[i])
                if counter2 == 0:
                    finalheader.insert(0, 'CgIdentifier')
                    finalheader.insert(1, 'GeneID')
                    counter2 += 1
            counter += 1
        else:
            methylationdata.append(row)


    for x in significantRegions:
        for y in methylationdata:
            if x[2] == y[0]:
                # locationdata.insert(0, x)
                y.insert(0, x[0])
                y.insert(1, x[1])
                locationdata.append(y)
    # Consider using hash (dictionaries to store the chr_loc: data)

    preID = methylationPerBase(locationdata)

finalCommit = locationdata

writeWHeader(finalCommit, finalheader)