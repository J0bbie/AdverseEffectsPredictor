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
parser.add_argument("-l", "--labelMapping", dest="labelMapping", default="label_mapping.tsv",
                  help="Give file name of the label_mapping.tsv if different.")

parser.add_argument("-a", "--adverseEffect", dest="adverseEffect", default="meddra_adverse_effects.tsv",
                  help="Give file name of the meddra_adverse_effects.tsv if different.")

parser.add_argument("-f", "--adverseFreq", dest="adverseFreq", default="meddra_freq_parsed.tsv",
                  help="Give file name of the meddra_freq_parsed.tsv if different.")

# Add a mutually exclusive group to overwrite/append/skip data that is already found in the SIDER2 DB
CRUDGroup = parser.add_mutually_exclusive_group(required=True)
CRUDGroup.add_argument('--overwrite', action='store_true')
CRUDGroup.add_argument('--skip', action='store_true')
CRUDGroup.add_argument('--append', action='store_true') #Standard option

#Parse the options
args = parser.parse_args()
arguments = vars(args)

#Debug arguments list
#print(arguments)

#######################################################
#                       Exceptions                    #
#######################################################

#Exception if there is a problem linking records from the file together (missing/incorrect STITCH etc.)
class noRelationException(Exception):
    pass

#######################################################
#                       Connections                   #
#######################################################

# Make the connection to the MYSQL server, using the settings in the setting.py file
# The SCHEMAS will be used to query to needed database
dbCon = pymysql.connect(host=s.databaseSettings['HOST'],
                                   port=s.databaseSettings['PORT'],
                                   user=s.databaseSettings['USER'],
                                   passwd=s.databaseSettings['PASSWORD'],
                                   autocommit = False)
# Create dbCursor to handle requests
dbCursor= connection.dbCursor()

#######################################################
#                   File handling                     #
#######################################################

# Try to make a file handler for all the required files

# Create filehandlers for the required files
# Open label mapping (contains the compounds (brand name + generic names and the label identifier + STITCH ID used in the other files)
labelMappingFile = open(os.path.join(arguments['inputDirectory'], arguments['labelMapping']),"r")
# Open medDRA adverse to get all the adverse effects for each compound (linked on STITCH ids)
meddraAdverseFile = open(os.path.join(arguments['inputDirectory'], arguments['adverseEffect']),"r")
# Open medDRA frequency file containing the frequencies of the adverse effects (linked on STITCH id)
meddraFreqFile = open(os.path.join(arguments['inputDirectory'], arguments['adverseFreq']),"r")
 
#######################################################
#                   File reading                      #
#######################################################

# The correct way to read is: label_mapping -> meddra_adverse_effects -> meddra_freq_parsed
writeLabelMapping(dbCon, dbCursor, arguments['CRUDGroup'], labelMappingFile)
writeMeddraAdverseEffects(dbCon, dbCursor, arguments['CRUDGroup'], meddraAdverseFile)
writeMeddraFreqParsed(dbCon, dbCursor, arguments['CRUDGroup'], meddraFreqFile)

# Write the contents from label_mapping.tsv to the DB, according to the set CRUD paramater, skip/append/overwrite identical records
def writeLabelMapping(dbCon, dbCursor, CRUDOption, file):
    for line in file:
        # Strip and split the line on tab and put the content in 7 variables
        (brandNames, substanceNames, STITCHMap, flatSTITCH, stereoSTITCH, urlEvidence, labelIdentifier) = line.strip().split('\t')
        
        # Try to find the compound that was used for this record (If a combination is used, multiple idCompound will be returned)
        # Use the subtance names names as they refer to the individual compounds
        idCompoundList = getCreateCompound(dbCon, dbCursor, substanceNames, STITCHMap)
        
        # Create the label record (based on CRUD skip/append/overwrite existing one)
        getCreateLabelRecord()
    
#Write the meddra_adverse_effects.tsv to the DB
def writeMeddraAdverseEffects(dbCon, dbCursor, CRUDOption, file):
    print("foo")
    
#Write the meddra_freq_parsed.tsv to the DB
def writeMeddraFreqParsed(dbCon, dbCursor, CRUDOption, file):
    print("foo")
    
# Try to retrieve the id of the compound from the compoundDB, else create it.
# Searching can be done with synonyms (brand+generic names etc.)
def getCreateCompound(connection, dbCursor, compoundNames):
    sqlQuery = "SELECT idCompound FROM normdb.tCompound as c LEFT JOIN tCompoundSynonyms ON c.idCompound = tCompoundSynonyms.idCompound WHERE %s OR %s LIMIT 1" % ('name = ', 'synonym =')
    pass

# Try to retrieve an existing medDRA term 
# SIDER2 shows both a LLT and/or PT for each adverse effect
def getCreateUpdateMedDRA(connection, dbCursor, medDRAPT, medDRALLT):
    pass