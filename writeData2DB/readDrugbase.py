# Author(s):    Job van Riet
# Date of  creation:    30-4-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This script can read a .sdf file from DrugBase containing names/synonyms of medicines, structures and structure mechanics such as ALOGP etc.

from optparse import OptionParser
import os

# Get the command line parameters
parser = OptionParser()
parser.add_option("-f", "--inputDirectory", dest="inputDirectory", default=os.path.dirname(os.path.realpath(__file__)),
                  help="Give the input directory containing ALL the files from FAERS")

(options, args) = parser.parse_args()
