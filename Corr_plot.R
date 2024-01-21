library(corrplot)
library(Hmisc)

phenos <- read.table(file = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/phenos_RRBS.txt", header = TRUE)
user_input = readline("Enter File Path: ")
cpgRegions <- read.csv(file = user_input, header = TRUE)

cpgRegions.t <-  t(cpgRegions)
age = phenos$dem_pat_age
chrname <- list()
identifier <- list()
geneid <- list()
chrname[1] <- "Age"
identifier[1] <- ''

age_list <-c(0, 0, 0, 75, 67, 71, 80, 69, 70, 62, 64, 73, 76, 67, 82, 52, 77, 87, 58, 75, 57, 65, 71, 76, 71, 62, 60, 66, 78, 74, 75, 60, 52, 80, 61, 92, 83, 79, 76, 71, 63, 72, 49, 89, 87, 67, 61, 76, 62)
d.f <- cpgRegions.t

data_matrix <- cbind( age_list, d.f[, (0 + 1):ncol(d.f)])

for(i in (1:length(cpgRegions.t[1,]))){
   chrname_temp <- as.character(cpgRegions.t[3,i])
   chrname <-append(chrname, chrname_temp)
   identifier_temp <- as.character(cpgRegions.t[1,i])
   identifier <- append(identifier, identifier_temp)
   geneid_temp <- as.character(cpgRegions.t[2,i])
   geneid <- append(geneid, geneid_temp)
}
colnames(data_matrix) <- NULL
# chrname <- append('0', chrname)
colnames(data_matrix) <- chrname

sampleIDs <- list()
sampleIDs <- rownames(data_matrix)

rrbs.m <- apply(as.matrix(data_matrix), 2, as.numeric)

rownames(rrbs.m) <- sampleIDs
rrbs.m <- rrbs.m[-1,]
rrbs.m <- rrbs.m[-1,]

cor_matrix <- rcorr(rrbs.m,type="spearman")

str(cor_matrix)

p <- cor_matrix$P

p.df <- as.data.frame(p)

chromLoc <- rownames(p.df)
identifier <- unlist(identifier)

p.df.age <- data.frame(ID = identifier,ChrLoc= chromLoc,age.p = p.df$Age)

head(p.df.age)

p.o.age <- p.df.age[order(p.df.age$age.p, decreasing = TRUE),]

p.o.age[1:20,1:3]
# prints first 20 rows of the p.o.age (ordered in ascending order)

write.table(p.o.age,file="p.values.age.cpg.txt")


png("corrPlot_CpG_SigReg.png",height=2000,width=2000,res=300)
corrplot(cor_matrix$P,order="hclust", tl.pos = 'n')
# corrplot(cor_matrix$P,diag = FALSE, order="hclust",  tl.pos='n')
# Error need a matrix or dataframe cor_matrix is a list of 3 matrices. Im passing it the cor_matrix$P
dev.off()


