# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This script can read the SIDER2 files and upload the data to the DB

from optparse import OptionParser
import os

# Get the command line parameters
parser = OptionParser()
parser.add_option("-f", "--inputDirectory", dest="inputDirectory", default=os.path.dirname(os.path.realpath(__file__)),
                  help="Give the input directory containing ALL the files from SIDER2 in .tsv format.")

#Parse the options
(options, args) = parser.parse_args()
arguments = vars(options)

arguments['inputDirectory'] = "C:/Users/rietjv/AppData/Local/My Local Documents/SIDER2/originalFiles/"

#Locate the files in the directory
for file in os.listdir(arguments['inputDirectory']):
    if file.endswith(".tsv"):
        if(file == "label_mapping.tsv"):
            print(file)


#Write the label_mapping.tsv to the DB
#Contains the compound labels used in the SIDER2 DB
def writeLabelMapping(filePath):
    print("foo")
    
#Write the meddra_adverse_effects.tsv to the DB
def meddraAdverseEffects(filePath):
    print("foo")
    
#Write the adverse_effects_raw.tsv to the DB
def adverseEffectsRaw(filePath):
    print("foo")
    
#Write the indications_raw.tsv to the DB
def indicationsRaw(filePath):
    print("foo")
    
#Write the meddra_freq_parsed.tsv to the DB
def meddraFreqParsed(filePath):
    print("foo")