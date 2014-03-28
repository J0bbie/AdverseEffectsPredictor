#Author:  Job van Riet
#Date of  creation:	28-3-14
#Date of modification:	28-3-14
#Version:	1.0
#Modifications:	Original version
#Known bugs:	None known
#Function:	
#This script correlates chemical compounds to adverse effects found in similar compounds.
#The correlation is based on binary chemical fingerprints and gene-expression/omics profiles.

#####################################################################################################
#                                       Main Process flow                                          #
#####################################################################################################

#####################################################################################################
#                             Load additional scripts, packages and parameters                      #
#####################################################################################################

#Keep track of the running time of this script.
ptm <- proc.time()

#Functions to get the passed parameters and set the default values of all parameters used in this pipeline
source(paste(SCRIPT.DIR,"getArguments.R",sep="/"))

#Get the command-line parameters that were given to this script (Parameters defined in getArguments.R)
#Also check the validity of these parameters and directories
userParameters <- getArguments(commandArgs(trailingOnly = TRUE))

#Function to install missing libraries
source(paste(userParameters$scriptDir,"functions_loadPackages.R",sep="/"))

#Functions for the creation of the plots
source(paste(userParameters$scriptDir,"functions_makeImages.R",sep="/"))

#Functions for the correlation of the fingerprints and gene-expression profiles to adverse effects
source(paste(userParameters$scriptDir,"functions_adverseCorrelation.R",sep="/"))

cat("\nLoading required packages.\n")

#Create a list of the mandatory packages needed for this pipeline.
pkgs <- c( "bioDist", "fingerprint" ,"gplots", "Category", "pcaMethods")

#Install any missing R libraries if needed
loadPackages(pkgs)

cat("\nRequired packages succesfully loaded.\n")

##################################################################################
##     	          Load the file containing the compounds 			##
##################################################################################

compFile = paste(userParameters$outputDir, userParameters$compoundList, sep = "")

cat("\nReading the compounds properties of all similar compounds:", compFile, "\n", sep="")

similarCompounds <- read.table(compFile,
                               header=T,  
                               stringsAsFactors = F,
                               sep='\t',
                               quote="")

cat("\nCompounds successfully loaded.\n")

##################################################################################
##     	Load the file containing the fingerprints of the structures	 	##
##################################################################################

if(userParamaters$useChemFingerPrints){
          chemFingerFile = paste(userParameters$outputDir, userParameters$chemFingerPrintFile, sep = "")
          
          cat("\nReading the chemical fingerprints of all the similar compounds:", chemFingerFile, "\n", sep="")
          
          similarCompounds <- read.table(compFile,
                                         header=T,  
                                         stringsAsFactors = F,
                                         sep='\t',
                                         quote="")
          
          cat("\nChemical fingerprints successfully loaded.\n")
}else{
          cat("\nSkipping correlation based on chemical fingerprints\n")
}

##################################################################################
##        Load the files containing the gene-expression profiles 		##
##################################################################################

#If normalization is true:
if(userParameters$useOmics){
          omicsFile = paste(userParameters$outputDir, userParameters$omicsFile, sep = "")
          
          cat("\nReading the gene-expressions profiles of all similar compounds:", omicsFile, "\n", sep="")
          
          description <- read.table(omicsFile,
                                    header=T,  
                                    stringsAsFactors = F,
                                    sep='\t',
                                    quote="")
          
          cat("\nGene expression profiles successfully loaded.\n")
}else{
          cat("\nSkipping correlation based on gene-expression profiles.\n")
}

##################################################################################
##        Correlate compounds based on the chemical fingerprints only		##
##################################################################################


cat("Correlation of compound to similar compounds is complete!")