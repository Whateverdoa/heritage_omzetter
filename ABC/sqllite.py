import sqlite3

# connection to database

conn = sqlite3.connect("mej_check.db")

# create cursor
cur = conn.cursor()

# # build a schema cq tables
# cur.execute("""CREATE TABLE check_orders(
#                 order_nummer TEXT,
#                 date_time TEXT,
#                 mej_gemaakt TEXT )
# """)


conn.commit()

conn.close()