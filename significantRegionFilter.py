import csv
from combineName import *

with open("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ_Chr__info_combined.csv") as file:
    combinedNames = csv.reader(file)
    # Call the method not the file and get filepath from CheckMatch.py

    with open("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ.csv", 'r') as file:
        # Set filepath as the first provided file path
        dataset = csv.reader(file)

        locdata = []
        combnam = []
        datst = []
        counter = 0

        for row in combinedNames:
            combnam.append(row)

        for row in dataset:
            datst.append(row)


        for x in combnam:
            for y in datst:
                if x[0] == y[0]:
                    locdata.append(y)
        print(locdata)

        header = ['', 'X2003_mtr.gz', 'X2005_mtr.gz', 'X2008_mtr.gz', 'X2012_mtr.gz', 'X2013_mtr.gz', 'X2014_mtr.gz', 'X2019_mtr.gz', 'X2020_mtr.gz', 'X2021_mtr.gz', 'X2026_mtr.gz', 'X2027_mtr.gz', 'X2028_mtr.gz', 'X2029_mtr.gz', 'X2031_mtr.gz', 'X2032_mtr.gz', 'X2034_mtr.gz', 'X2036_mtr.gz', 'X2040_mtr.gz', 'X2043_mtr.gz', 'X2046_mtr.gz', 'X2047_mtr.gz', 'X2049_mtr.gz', 'X1010.D28_mtr.gz', 'X1012.D28_mtr.gz', 'X1014.D28_mtr.gz', 'X1017.D28_mtr.gz', 'X1028.D28_mtr.gz', 'X1030.D28_mtr.gz', 'X1032.D28_mtr.gz', 'X1045.D28_mtr.gz', 'X1047.D28_mtr.gz', 'X1054.D28_mtr.gz', 'X1055.D28_mtr.gz', 'X1060.D28_mtr.gz', 'X1061.D28_mtr.gz', 'X1067.D28_mtr.gz', 'X1068.D28_mtr.gz', 'X1070.D28_mtr.gz', 'X1086.D28_mtr.gz', 'X3001.D28_mtr.gz', 'X3005.D28_mtr.gz', 'X3012.D28_mtr.gz', 'X3015.D28_mtr.gz', 'X3018.D28_mtr.gz', 'X3019.D28_mtr.gz', 'X3032.D28_mtr.gz']
        # extract header from the first provided file
        with open("intron_ShrunkenSignificantRegionsData.csv", 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
            csvwriter.writerows(locdata)


