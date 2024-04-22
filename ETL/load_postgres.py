import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2.extras as extras
import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DBNAME, HOST, POSTGRES_SCHEMA

# Asks for path to folder
folder = input("Enter the folder path: ")

conn_params_dic = {
    "host"      : HOST,
    "database"  : POSTGRES_DBNAME,
    "user"      : POSTGRES_USER,
    "password"  : POSTGRES_PASSWORD
}

# Define a connect function for PostgreSQL database server
def connect(conn_params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL...........')
        conn = psycopg2.connect(**conn_params_dic)
        print("Connection successfull.................")
        print(">>>>>>")
        
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)        
        # set the connection to 'None' in case of error
        conn = None
    return conn


# Define a function that handles and parses psycopg2 exceptions
def show_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()    
    # get the line number when exception occured
    line_n = traceback.tb_lineno    
    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type) 
    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)    
    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

# sqlalchemy
# create_engine('dialect+driver://user:pass@host:port/db')
connect_alchemy = "postgresql+psycopg2://%s:%s@%s/%s" % (
    conn_params_dic['user'],
    conn_params_dic['password'],
    conn_params_dic['host'],
    conn_params_dic['database']
)


def load_to_db(folder):
    try:
        for file in os.listdir(folder):
            if file.endswith('.csv'):  
                file_path = os.path.join(folder, file)
                df = pd.read_csv(file_path)
                engine = create_engine(connect_alchemy)
                df.to_sql(file.replace('.csv',''), con=engine, schema=POSTGRES_SCHEMA, if_exists='replace', index=False)
        print("Files loaded to Postgres successfully...")
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)
        cursor.close()

#--------------------------------------------------------------------------------
# RUN
#--------------------------------------------------------------------------------
        
conn = connect(conn_params_dic)
# We set autocommit=True so every command we execute will produce results immediately.
conn.autocommit = True
cursor = conn.cursor()

# Closing the cursor & connection
cursor.close()
conn.close()

if __name__ == "__main__":
    load_to_db(folder)       