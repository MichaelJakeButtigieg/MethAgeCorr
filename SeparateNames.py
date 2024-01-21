import csv

filepath = ""
matrix = []

def separatenames(filepath):

    with open(filepath, 'r') as file:
        data = csv.reader(file)

        final = []

        for row in data:
            hold = row
            sthold= str(hold[0])
            separated = sthold.split("_")
            final.append(separated)

        return (final)

def separateName(matrix):

    final = []

    for row in matrix:
        hold = row
        sthold = str(hold[0])
        separated = sthold.split("_")
        final.append(separated)

    return(final)
# header = ['Chr', 'Start', 'End']
#
#
#
# with open("RRBS_filt_CpG_AgeQ_Chr_info_separated.csv", 'w') as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow(header)
#     csvwriter.writerows(separatenames("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/RRBS_filt_CpG_AgeQ.csv"))

# Function to write out the separated columns in a .csv file (Not Necessary as you can just call the separatenames()


