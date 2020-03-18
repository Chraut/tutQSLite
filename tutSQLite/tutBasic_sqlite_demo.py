'''
Created on Mar 18, 2020

@author: marbe
'''

import sqlite3
from employee import Employee

#conn = sqlite3.connect(':memory:')     # just for RAM database (good for testing every time a new db)
conn = sqlite3.connect('employee.db')   # either it creates the file or
                                        # when exist connect to it

c = conn.cursor()                       # create cursor (always)

'''                                     # only for creation
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer    
            )""")
'''

'''                                     # possible to enter one row
c.execute("INSERT INTO employees VALUES ('Mary','Schafer',70000)") 
conn.commit()  
'''

'''
c.execute("SELECT * FROM employees WHERE last='Schafer'")
c.fetchone()                            # selects only one entry
c.fetchall()                            # selects all from this point
fetchmany(5)                            # return that number of row as a list
'''

emp_1 = Employee("John", "Doe", 80000)
emp_2 = Employee("Jane", "Doe", 90000)

'''                                    # write values
# actually wrong because db can be breaked
c.execute("INSERT INTO employees VALUES ('{}','{}',{})", (emp_1.first, emp_1.last, emp_1.pay)) 

# correct
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay)) 

# best
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay})

conn.commit() 
'''

'''                                     # read values
                                        # for select no commit, close, update needed
c.execute("SELECT * FROM employees WHERE last='Schafer'")
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(c.fetchall())
'''

conn.commit()                            # must for every change!

conn.close()