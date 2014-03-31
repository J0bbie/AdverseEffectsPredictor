# Author(s):    Job van Riet
# Date of  creation:    27-3-14
# Date of modification:    Initial version
# Version:    1.0
# Modifications:    None
# Known bugs:    None Known
# Function:
# This file houses the functions to write the various data to the database.

# Import user specified settings
import writeData2DB.settings as s

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
        
    def query(self):
        self.cursor.execute()
    
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
        
    # Try to find if the meDRA term already exists and retrieve that ID or create a new meDRA term and return the newly create (Auto-increment) key
    def createGetMedRA(self, name, conceptType="NULL", idUMLS="NULL"):
        self.cursor.execute("SELECT idMedRA FROM tMedRA WHERE name LIKE %s;", ("%" + name + "%"))
        idMedRA = self.cursor.fetchone()
        
        # Create if not already existing
        if not idMedRA:
            self.cursor.execute("INSERT INTO tMedRA (name, conceptType, idUMLS) VALUES ( %s, %s, %s);", name, conceptType, idUMLS)
            idMedRA = self.connection.insert_id()
            
        # Return the ID of the meDRA term
        return(idMedRA)

    # Try to find if the compound already exists and retrieve that ID or create a new compound and return the newly create (Auto-increment) key
    def createGetCompound(self, name, description="NULL"):
        self.cursor.execute("SELECT c.idCompound FROM compoundDB.tCompound as c JOIN compoundDB.tSynonyms as s WHERE c.name LIKE %s OR s.name LIKE %s ", ("%" + name + "%"), ("%" + name + "%"))
        idCompound = self.cursor.fetchone()
        
        # Create if not already existing
        if not idCompound:
            self.cursor.execute("INSERT INTO compoundDB.tCompound (name) VALUES ( %s);", name)
            idCompound = self.connection.insert_id()
            
        # Return the ID of the compound
        return(idCompound)