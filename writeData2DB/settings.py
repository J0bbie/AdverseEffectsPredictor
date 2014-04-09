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

# Change this to a user/schema with INSERT permissions and the correct fields.
# For simplicity sake, the same user is used for all the databases.
databaseSettings = dict(
    # IP/Hostname of MySQL server
    HOST='127.0.0.1',  # 127.0.0.1
    # Port for connecting to MySQL
    PORT=3306,  # 3306
    # MySQL User
    USER='job',  # job
    # Password for MySQL user
    PASSWORD='jobPass',  # jobPass
    # Schema which houses the database for the SIDER2 data
    SCHEMASIDER='SIDER2',  # SIDER2
    # Schema which houses the database for the FAERS data
    SCHEMAFAERS='FAERS',  # FAERS
    # Schema which houses the database for the PROTECTADR data
    SCHEMAPROTECTADR='protectADR',  # protectADR
    # Schema which houses the database for the medDRA data
    SCHEMAMEDDRA='medDRA'  # medDRA
)

