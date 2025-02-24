import sqlite3
from sympy import pi, N

conn = sqlite3.connect('math.db')
cursor = conn.cursor()

#This is initial setup of the pimem, it should not be packaged, since the database should be prepopulated with the pi-digits
def pi_table():
    #THIS ISN'T ACTUALLY USED, JUST SAVING THE DATABASE SCHEMA HERE
    conn.execute('''CREATE TABLE IF NOT EXISTS pi_chunks
                        (chunk_digits TEXT,
                        memorized INTEGER DEFAULT 0,
                        memorized_date TEXT,
                        )''')
    conn.commit()

def insert_chunks(cursor):
    num_digits = 202 #account for removing 3., assuming the . is considered a digit - can be set to any arbitrarily large range 
    pi_digits = str(N(pi, num_digits))#[2:] remove first two digits
    for i in range(0, num_digits, 6):
        chunk = pi_digits[i:i+6]
        cursor.execute("INSERT INTO pi_chunks (chunk_digits) VALUES (?)", (chunk,))
        conn.commit()
    conn.close()

def twohundred_checker():
    cursor.execute('''SELECT rowid,chunk_digits FROM pi_chunks WHERE rowid = 34 LIMIT 1''')
    pre_check = cursor.fetchall()
    conn.close()
    rowid, value = pre_check[0]
    if rowid == 34 and value == '81964':
        print("Database already contains 200 digits of pi.")
    else:
        return('Table of pi digits is not found.')

def k_checker():#try except here
    cursor.execute('''SELECT rowid,chunk_digits FROM pi_chunks WHERE rowid = 167 LIMIT 1''')
    pre_check = cursor.fetchall()
    conn.close()
    rowid, value = pre_check[0]
    if rowid == 167 and value == '19894':
        print("Database already contains 1,000 digits of pi.")
    else:
        print('Table of pi digits is not found.')
    
if __name__== "__main__":
    #k_checker()
    #insert_chunks(cursor)
    twohundred_checker()
    