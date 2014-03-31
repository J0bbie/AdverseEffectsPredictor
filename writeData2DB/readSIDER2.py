# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This script can read the SIDER2 files and upload the data to the DB

#Import command line parser
from optparse import OptionParser

#Import os options (read dir/extensions)
import os

# Import user specified settings
import writeData2DB.settings as s

# Import MySQL functions
import pymysql

# Get the command line parameters
parser = OptionParser()
parser.add_option("-f", "--inputDirectory", dest="inputDirectory", default=os.path.dirname(os.path.realpath(__file__)),
                  help="Give the input directory containing ALL the files from SIDER2 in .tsv format.")

#Parse the options
(options, args) = parser.parse_args()
arguments = vars(options)

arguments['inputDirectory'] = "C:/Users/rietjv/AppData/Local/My Local Documents/SIDER2/originalFiles/"

#######################################################
#                       Exceptions                    #
#######################################################

#Exception if one of the five required files is not present in the input directory
class reqFileException(Exception):
    pass

#Make the connection to the DB, using the settings in the setting.py file
connection = pymysql.connect(host=s.databaseSettings['HOST'],
                                     port=s.databaseSettings['PORT'],
                                     user=s.databaseSettings['USER'],
                                     passwd=s.databaseSettings['PASSWORD'],
                                     db=s.databaseSettings['SCHEMA'],
                                     autocommit = False)
# Create cursor to handle requests
cursor = connection.cursor()

#######################################################
#                   File searching                    #
#######################################################

#Locate the files in the directory
for file in os.listdir(arguments['inputDirectory']):
    if file.endswith(".tsv"):
        try:
            #First find the label_mapping.tsv file as this contains the compounds (brand name + generic names and the label identifier used in the other files)
            if(file == "meddra_adverse_effects.tsv"):
                print("foo")
            else:
                raise reqFileException("Could not locate label_mapping.tsv in directory: "+arguments['inputDirectory'])
        #If one of the required files could not be located
        except reqFileException:
            #Rollback the database to prevent half-complete data inserts
            connection.rollback()

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