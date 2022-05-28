import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSAHALQASIM;'
                      'Database=Demo;'
                      'Trusted_Connection=yes;'
                      'uid=sa;pwd=Optiplex@242244')

cursor = conn.cursor()
cursor.execute('SELECT Name FROM EMP')

for i in cursor:
    print(i)