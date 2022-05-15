def create_db(conf, conn):
    cursor = conn.cursor()
    conn.autocommit = True
    createdb_query = "CREATE DATABASE {0}".format(conf['database'])
    cursor.execute(createdb_query) # execute the table creation query
    cursor.close()

def create_table(conn):
    cursor = conn.cursor()
    conn.autocommit = True
    try:
        createtable_query = open("create_table.sql")
        cursor.execute(createtable_query.read()) # execute the table creation query
    except Exception as e:
        print(e)
        conn.rollback() # undo the transactions that have not been saved in the database
    cursor.close()

def insert_data(conn, columns, values):
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        insert_query = "INSERT INTO tweets({0}) VALUES {1};".format(columns, tuple(values))
        cursor.execute(insert_query)
    except Exception as e:
        print(e)
        conn.rollback()
    cursor.close()


