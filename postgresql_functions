""" Work with PostgreSQL with 'psycorg2' module
    http://www.psycopg.org/psycopg/docs/module.html#module-psycopg2 """
import psycopg2

# Create a new database session
db_conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="secret", dbname="test")
db_conn = psycopg2.connect("dbname=eat user=1")


# Create a new cursor
# http://www.psycopg.org/psycopg/docs/cursor.html
db_cursor = db_conn.cursor()

# Execute a database operation (query or command).
db_cursor.execute("SELECT * FROM person WHERE id = %s;", (123,))

# Get one result row
res = db_cursor.fetchone()
