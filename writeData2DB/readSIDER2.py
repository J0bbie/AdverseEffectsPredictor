# Author(s):    Job van Riet + Data from SIDER2/ChEMBL
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This script can read the SIDER2 files and upload the data to the DB
# It uploads the contents into a schema designed for SIDER2 data, making use of a compound DB to store the compound and a medDRA database to store the medDRA terms
# The following files are used: label_mapping, meddra_adverse_effects and meddra_freq_parsed files from SIDER2 in .tsv format.

#Import command line parser
import argparse

#Import os options (read dir/extensions)
import os

# Import user specified settings for connecting to the DB
import settings as s

# Import MySQL functions
import pymysql

# Get the command line parameters

parser = argparse.ArgumentParser(description='Write SIDER(2) data into the DB')
parser.add_argument("-i", "--inputDirectory", dest="inputDirectory", default=os.path.dirname(os.path.realpath(__file__)),
                  help="Give the input directory containing the label_mapping, meddra_adverse_effects and meddra_freq_parsed files from SIDER2 in .tsv format.")

# If the files has different names, supply them with these parameters
parser.add_argument("-l", "--labelMapping", dest="inputDirectory", default="label_mapping.tsv",
                  help="Give file name of the label_mapping.tsv if different.")

parser.add_argument("-a", "--adverseEffect", dest="adverseEffect", default="meddra_adverse_effects.tsv",
                  help="Give file name of the meddra_adverse_effects.tsv if different.")

parser.add_argument("-f", "--adverseFreq", dest="adverseFreq", default="meddra_freq_parsed.tsv",
                  help="Give file name of the meddra_freq_parsed.tsv if different.")

# Add a mutually exclusive group to overwrite/append/skip data that is already found in the SIDER2 DB
CRUDGroup = parser.add_mutually_exclusive_group()
CRUDGroup.add_argument('--overwrite', action='store_true')
CRUDGroup.add_argument('--skip', action='store_true')
CRUDGroup.add_argument('--append', action='store_true')

#Parse the options
args = parser.parse_args()
arguments = vars(args)

#print(arguments['inputDirectory'])

#######################################################
#                       Exceptions                    #
#######################################################

#Exception if one of the five required files is not present in the input directory
class reqFileException(Exception):
    pass

#######################################################
#                       Connections                   #
#######################################################

# Make the connection to the MYSQL server, using the settings in the setting.py file
# The SCHEMAS will be used to query to needed database
connection2SIDER = pymysql.connect(host=s.databaseSettings['HOST'],
                                     port=s.databaseSettings['PORT'],
                                     user=s.databaseSettings['USER'],
                                     passwd=s.databaseSettings['PASSWORD'],
                                     db=s.databaseSettings['SCHEMASIDER'],
                                     autocommit = False)
# Create cursor to handle requests
cursor= connection.cursor()

#######################################################
#                   File searching                    #
#######################################################

#Open the files in the correct order (Label_mapping -> meddra_adverse_effects -> meddra_freq_parsed)
try:
    #First find the label_mapping.tsv file as this contains the compounds (brand name + generic names and the label identifier + STITCH ID used in the other files)
    if(file == "label_mapping.tsv"):
        filePath = '/'.join(arguments['inputDirectory'], "label_mapping.tsv")
        #Read the contents 
        writeLabelMapping(filePath)
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
    
#Write the meddra_freq_parsed.tsv to the DB
def meddraFreqParsed(filePath):
    print("foo")
    
# Try to retrieve the id of the compound from the compoundDB, else create it.
# Searching can be done with synonyms (brand+generic names etc.)
def getCreateCompound(connection, cursor, compoundNames):
    sqlQuery = "SELECT idCompound FROM normdb.tCompound as c LEFT JOIN tCompoundSynonyms ON c.idCompound = tCompoundSynonyms.idCompound WHERE %s OR %s LIMIT 1" %
    ('name = ')

    pass

# Try to retrieve an existing medDRA term 
# SIDER2 shows both a LLT and/or PT for each adverse effect
def getCreateUpdateMedDRA(connection, cursor, medDRAPT, medDRALLT):
    pass