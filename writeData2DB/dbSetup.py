# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This file houses the functions to write the various data to the database.

# Import user specified settings
import toxicData2DB.settings as s

# Import MySQL functions
import pymysql

############################
#    dbConnection Class    #
############################

class dbConnection:
    def __init__(self):
        self.connection
        self.cursor
    
    # On death of object, still close the connection to prevent open connections
    def __del__(self):
        self.closeConnection(self)

    # Creates a connection to the MySQL database using the setting in settings module
    # Returns a cursor based on user specified setting in the setting.py file
    def createConnection(self):
        # Make connection to MySQL DB
        self.connection = pymysql.connect(host=s.databaseSettings['HOST'],
                                     port=s.databaseSettings['PORT'],
                                     user=s.databaseSettings['USER'],
                                     passwd=s.databaseSettings['PASSWORD'],
                                     db=s.databaseSettings['SCHEMA'])
        
        # Create cursor to handle requests
        self.cursor = self.connection.cursor()
    
    # Close the connection manually
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
    
    # Commit the data to DB
    def commit(self):
        self.connection.commit()
        
    # Rollback DB (On error for instance)
    def rollback(self):
        self.connection.rollback()
    
    ##########################
    #    Write2DB methods    #
    ##########################
    
    # Try to find if the adverse effect already exists and retrieve that ID or create a new adverse effect and return the newly create (Auto-increment) key
    def createGetAdverseEffect(self, name, description="NULL"):
        self.cursor.execute("SELECT idAdverseEffect FROM tAdverseEffect WHERE name LIKE %s;", ("%" + name + "%"))
        idAdverseEffect = self.cursor.fetchone()
        
        # Create if not already existing
        if not idAdverseEffect:
            self.cursor.execute("INSERT INTO tAdverseEffect (name, description) VALUES ( %s, %s);", name, description)
            idAdverseEffect = self.connection.insert_id()
            
        # Return the ID of the adverse effect
        return(idAdverseEffect)
        
    # Try to find if the adverse effect already exists and retrieve that ID or create a new adverse effect and return the newly create (Auto-increment) key
    def createGetMedRA(self, name, conceptType="NULL", idUMLS="NULL"):
        self.cursor.execute("SELECT idMedRA FROM tMedRA WHERE name LIKE %s;", ("%" + name + "%"))
        idMedRA = self.cursor.fetchone()
        
        # Create if not already existing
        if not idMedRA:
            self.cursor.execute("INSERT INTO tMedRA (name, conceptType, idUMLS) VALUES ( %s, %s, %s);", name, conceptType, idUMLS)
            idMedRA = self.connection.insert_id()
            
        # Return the ID of the adverse effect
        return(idMedRA)
