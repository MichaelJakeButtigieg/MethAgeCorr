import csv

filepath = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ_SignificantRegions.csv"
resultList = []


def combineNamesFile(filepath):

    with open(filepath, 'r') as file:
        idandlist = csv.reader(file)

        final = []

        for row in idandlist:
            chr = row[1]
            chrstart = row[2]
            chrend = row[3]
            chrloc= chr + "_" + chrstart + "_" + chrend
            chrlocst = str(chrloc)
            # print(chrloc)
            final.append(chrlocst)
        # print(final[])
        return(final)

def combineNames(resultList):
    final = []

    for row in resultList:
        chr = row[1]
        chrstart = row[2]
        chrend = row[3]
        chrloc = chr + "_" + chrstart + "_" + chrend
        chrlocst = str(chrloc)
        final.append(chrlocst)

    # print(final[])
    return (final)




# towrite = combineNames(filepath)
# # header = ['CombChrandLoc']
#
# with open("RRBS_filt_CpG_AgeQ_Chr__info_combined.csv", 'w') as file:
#     csvwriter = csv.writer(file)
#     for i in range(0,len(towrite)):
#         csvwriter.writerow([towrite[i]])
#


    # print(combinedchrandloc)

#combineNames("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ_SignificantRegions.csv")
# print(combineNames("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ_SignificantRegions.csv"))