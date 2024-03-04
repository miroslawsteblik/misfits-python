# psycopg2-tutorial/config.py

from configparser import ConfigParser


def get_db_info(filename,section):
    ## instantiating the parser object
    # The function get_db_info() takes in the names of the config file and the section as arguments.
    # It returns the details of the database as a Python dictionary.
    parser=ConfigParser()
    parser.read(filename)

    db_info={}
    if parser.has_section(section):
         # items() method returns (key,value) tuples
         key_val_tuple = parser.items(section)
         for item in key_val_tuple:
             db_info[item[0]]=item[1] # index 0: key & index 1: value

    return db_info