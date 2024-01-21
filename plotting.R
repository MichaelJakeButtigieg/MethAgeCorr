library("ggplot2")
phenos <- read.table(file = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/phenos_RRBS.txt", header = TRUE)
user_input = readline("Enter File Path: ")
cpgRegions <- read.csv(file = user_input, header = TRUE)

cpgRegions.t <-  t(cpgRegions)
age = phenos$dem_pat_age
filter <- readline("What type of region is this (Intron, Gene, Exon, etc..")
plot_list = list()

pdf(file = "/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/CpG_AgevsMethRatio.pdf", onefile = TRUE)
  for(i in (1:length(cpgRegions.t[1,]))){

    chrname <- as.character(cpgRegions.t[3,i])
    GeneId <- as.character(cpgRegions.t[2,i])
    identifer <- as.character(cpgRegions.t[1,i])
    title = paste(filter, chrname, identifer, 'GeneID: ', GeneId)

    suppressWarnings(Methylation_Ratio <- as.numeric(cpgRegions.t[,i]))
    Methylation_Ratio <- Methylation_Ratio[-c(1:3)]
    # print(Methylation_Ratio)
    maximum <- max(Methylation_Ratio)
    maximum.r <- round(maximum, 5)

    d.f <- data.frame(x = age,y = Methylation_Ratio)
    # print(d.f)
    # p <- ggplot(data = d.f, mapping = aes(x = age, y = Methylation_Ratio)) + geom_point() + ggtitle(title)
    # print(p)

    p1 = ggplot(data = d.f, mapping = aes(x = age, y = Methylation_Ratio)) + geom_point() + ggtitle(title) + scale_y_continuous(limits=c(0.0000,maximum.r)) + scale_x_continuous(limits = c(50,100))
    print(p1)
    #Removeing missing values GoemPoint() IDK Y. Its not the NA and it shouldnt be out of range, the range is set by the max value
    # Scale for y axis set to a rounded up number from the maximum number present in the data frame
    # plot_list[[i]] = p1
    # print(plot_list[i])

    # p1 = ggplot(data = d.f, mapping = aes(x = age, y = Methylation_Ratio)) + geom_point() + ggtitle(title) + scale_y_continuous(limits=c(0.0000,0.00001)) + scale_x_continuous(limits = c(50,100))
    # print(p1)
  #   Preset scale for the Y axis

  }
dev.off()



#
  # pdf("/home/michaelj/Desktop/Coding/Thesis/CpGtoChrLoc/venv/lib/test.pdf") #
  # print(p)
  # dev.off()