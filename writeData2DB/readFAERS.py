# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This script can read the FAERS files and upload the data to the DB

from optparse import OptionParser
import os

# Get the command line parameters
parser = OptionParser()
parser.add_option("-f", "--inputDirectory", dest="inputDirectory", default=os.path.dirname(os.path.realpath(__file__)),
                  help="Give the input directory containing ALL the files from FAERS")

(options, args) = parser.parse_args()
