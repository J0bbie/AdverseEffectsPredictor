# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This file houses the constants that the user needs to adjust to allow for functionality in their environment

########################
#    MySQL Settings    #
########################

# Change this to a user/schema with INSERT permissions and the correct fields. (As shown in the ERD)
databaseSettings = dict(
    # IP/Hostname of MySQL server
    HOST='127.0.0.1',  # 127.0.0.1
    # Port for connecting to MySQL
    PORT=3306,  # 3306
    # MySQL User
    USER='jobDiamonds',  # job
    # Password for MySQL user
    PASSWORD='jobPass',  # jobPass
    # Schema which houses the database
    SCHEMA='adverseDB'  # adverseDB
)

