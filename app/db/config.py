#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class CreatureTable:

    NAME = "creatures"

    SCHEMA = """
        CREATE TABLE creatures (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            species TEXT NOT NULL,
            name    TEXT NOT NULL,
            image   TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO creatures (species, name, image)
        VALUES ("Raw Chicken",  "Bingus", "bingus.png")
    """

# Add more table classes here...

# ("Unicorn", "Barry", "barry.png"),
# ("Vampire", "Helen", "helen.png")

#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1,
#     Table2,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
#       foreign keys AFTER the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    CreatureTable,
    # Add more tables here...
]

