# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:06:33 2021

@author: lenovo
"""

import sys
import cx_Oracle
import pandas as pd

#connecting oracle
con=cx_Oracle.connect('system/shital07@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("connection done")
else:
    print("not done")
    
#excuting cursor
cur=con.cursor()

def displayall():
    cur.execute("select * from cust1")
    for row in cur.fetchall():
        print(row[0],"\t",row[1])
        
displayall()

#fetching table
table_rows = cur.fetchall()
df= pd.read_sql('select * from cust1', con)
df.set_index(['NAME'], inplace=True)


print(df)

def show_get_info(cntry):
    data = df.loc[df['COUNTRY'] == cntry]
    print(data)
    file = str(cntry)
    data.to_csv("D:/DBDA/DBMS/incubyte_test/" + file + ".csv")#copy csv to desired location
    print("file created")
 
#call function
show_get_info('AU')
    

