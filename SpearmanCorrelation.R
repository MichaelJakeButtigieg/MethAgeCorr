phenos <- read.table(file = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/phenos_RRBS.txt", header = TRUE)
user_input = readline("Enter File Path: ")
cpgRegions <- read.csv(file = user_input, header = TRUE)

cpgRegions.t <-  t(cpgRegions)
age = phenos$dem_pat_age
namesWrite <- list()
p_value <- list()
rho_value <- list()
identfier <- list()
geneid <- list()

for(i in (1:length(cpgRegions.t[1,]))){
  chrname <- as.character(cpgRegions.t[3,i])
  namesWrite <- append(namesWrite, chrname)
  # print(namesWrite)
  CgId <- as.character(cpgRegions.t[1,i])
  identfier <- append(identfier, CgId)
  # print(identfier)
  GID <- as.character(cpgRegions.t[2,i])
  geneid <- append(geneid,GID)
  suppressWarnings(methCol <- as.numeric(cpgRegions.t[,i]))
  methCol <- methCol[-c(1:3)]
  # Removing the introduced NA values (CgId ,geneID and ChrLoc) so that X = Age and Y = MethCol are of equal length
  towrite <- cor.test(x = age,y=methCol,method='spearman',exact = FALSE)
  p_value <- append(p_value, towrite$p.value)
  rho_value <- append(rho_value, towrite$estimate)

}

# for (i in (1:length(namesWrite))){
#   namesCommit <- c(namesWrite[i])
#   p_value_commit <- c(p_value[i])
# }

d.f <- data.frame(CGIdentifier = unlist(identfier),Gene_ID = unlist(geneid), Chromosome_Location = unlist(namesWrite), Spearman_P_Values = unlist(p_value), Rho_Value = unlist(rho_value))

d.f.o <- d.f[order(d.f$Spearman_P_Values, decreasing = FALSE),]

d.f.o.top <- d.f.o[1:20,]


write.csv(d.f.o, "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/CpG_Spearman_Correlations_Table.csv", row.names=FALSE)

write.csv(d.f.o.top, "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/CpG_Spearman_Correlations_Table_Top20.csv", row.names=FALSE)


# To create a  data matrix with methylation data and one column with age
#
# age <-c(0, age) #to make the list of age as long as the number of rows (samples) since the first row is the chr locations not methylation data
# rrbs.m <- cbind(age,cpgRegions.t) #makes a matrix in this order

# SampleID, Age, Chr1_xxx_xxx, Chr2_xxx_xxx, ....
# 2003.xx, 75, 0.071          , 0.0534      , ...
