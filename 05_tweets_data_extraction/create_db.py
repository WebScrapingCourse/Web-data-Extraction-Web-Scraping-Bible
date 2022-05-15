import psycopg2
from dao import  create_db, create_table
from utils import load_conf



if __name__ == "__main__":

    conf = load_conf("postgresql") # import the parameters for the connection
    psql_connection_string = "user={0}".format(conf['user'])
    conn = psycopg2.connect(psql_connection_string) # Connect to PostgreSQL
    create_db(conf, conn) # Create the tweets_db database

    # Connect to the database created
    conn_db = psycopg2.connect(**conf)

    # Create the tweets table
    create_table( conn_db)

    conn_db.close()  # Close connection to the database

