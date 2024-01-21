import csv
from SeparateNames import *

datasetChrloc = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ.csv"
# ASK FOR FILE PATH, so you can run it from terminal
data = separatenames(datasetChrloc)
# uses the separate names method : separatenames(filepath)
# results in dataframe with chromosome number start and end locations


with open("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/Hovarth_ UniqueID _ChrLoc.csv") as file:
    # Ask for filepath (regions_filter)
    regions = csv.reader(file)
    #contains the chromosomes and chromsome ranges (i.e. start and end locations) that we are looking for in the 'data'
    chrgroup = []
    fullagree = []
    within = []
    other = []

    for row in regions:
        regionrow = row
        # print(regionrow)
        chr = "chr" + str(row[1])
        # Adds "chr" in front of the chromosome number so thta it is consistent with the chromosome number in 'data'
        # Maybe should be the opposite, strip all text from the inputted files and leave only the chromosome number (thiswould require more exception)
        # print("Hov chr: " + chr)
        genstart = row[2]
        #print("Hov GenS: " + genstart)
        genend = row[3]
        #print("Hov GenE: " + genend)

        if genstart > genend:
            genstart = row[3]
            genend = row[2]
            #if genestart is larger than geneend swaps them to get the compliment chr locations (because all of the chromosome locations in the 'data' file are start > end


        for row in data:

            if str(row[0]) == chr:
                # if row[0] (the chr number) is = to the chr number of the chromosome region, append the row (chr, start, end) to a list (chrgroup)
                # This is here so that we don't check the start and end locations of 'data' regions not int the same chromosome.
                chrgroup.append(row)
                #puts the datapoints with the same chromosome as the region in a list

        for row in chrgroup:
                if row[1] == genstart and row[2] == genend:
                    row.insert(0, regionrow[0])
                    # inserts cg identifier (e.g. cg00000) at the beginning of row
                    fullagree.append(row)
                    #checks if the hovarth range and the 'data' range are exactly the same, if they are adds the row (chr,start,end) to the full agree list

                elif row[1] >= genstart and genend >= row[2]:
                    #checks if the 'data' range is within the hovarth range (row[1] = start loc, row[2] = endloc

                    check = int(row[1]) - int(genstart)
                    check2 = int(genend) - int(row[2])

                    if check > 0 and check2 > 0:
                        # checks if the 'data' range is within the hovarth range (row[1] = start loc, row[2] = endloc

                        row.insert(0, regionrow[0])
                        within.append(row)

                        header = ['CGidentifier', 'ChromosomeNumber', 'Start', 'End']
                        # Custimizable name of file
                        with open("RRBS_filt_CpG_AgeQ_SignificantRegions.csv", 'w') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            csvwriter.writerow(header)
                            csvwriter.writerows(within)
                            # writes everything into a .csv file
                    else:
                       #  ASk for input (Would you liek the non-significant regions as a separate .csv file
                       other.append(row)
                       row.insert(0, regionrow[0])

                       header = ['HovarthsIdentifier', 'ChromosomeNumber', 'Start', 'End']

                       with open("RRBS_filt_CpG_AgeQ_others.csv", 'w') as csvfile:
                           csvwriter = csv.writer(csvfile)
                           csvwriter.writerow(header)
                           csvwriter.writerows(other)
                           # writes everything into a .csv file


        #print("ChrGroup : " , chrgroup)
        chrgroup = []
        #print("Full agree: " , fullagree)
        #print("within :" , within)



