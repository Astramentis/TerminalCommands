import sqlite3
import numpy as np
from typing import TypeVar, Iterable, Tuple

#help(numpy)
conn = sqlite3.connect('src/math.db')
cursor = conn.cursor()

def main():
  arr1 = np.array([1, 2, 3, 4, 5],dtype=int)
  print(arr1)
  arr2 = np.random.randint(low=0, high=101, size=(1,3), dtype=int) #generate a single dimensional array (size) of 3 numbers between 0 and 100 (high is excluded) of whole intergers
  print(arr2)
  pass

def test():
    from sympy import pi, N
    pi_digits = str(N(pi, 200))
    print('launching 200 digits of pi')
    return(str(pi_digits))

def check_6(chunk_id):
    cursor.execute('''SELECT  chunk_digits FROM pi_chunks WHERE rowid = (?) LIMIT 1''',(chunk_id,))
    fetch = cursor.fetchone()
    chunk = str(fetch[0]) #ironically, doing these comparisons with strings is much easier because it prevents leading zeros (ex 089986) from being dropped 
    print(chunk)
    return(chunk)

def hint(chunk_id):
    cursor.execute('''SELECT  mhint_minor, mhint_major FROM pi_chunks WHERE rowid = (?)''',(chunk_id,))
    fetch = cursor.fetchone()
    mhint_minor, mhint_major = fetch[0:]
    return(mhint_minor, mhint_major)