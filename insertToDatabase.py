import mysql.connector
from mysql.connector import Error

#Update GeneralUser database
#Update PersonsData Table in the database


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpasswordgiven",
    database="GeneralUser"
    )

mycursor=mydb.cursor()

def insert_table(ID,IDNumber,long,lat,time,date):
 sqlFormula="INSERT INTO PersonsData (ID,IDNumber,longitude,latitude,timeData,dateData) VALUES (%s,%s,%s,%s,%s,%s)"
 personsname=(ID,IDNumber,long,lat,time,date)
 mycursor.execute(sqlFormula,personsname)
 mydb.commit()

def count_rows():
 sqlFormula=" SELECT COUNT(*) FROM PersonsData"
 mycursor.execute(sqlFormula)
 myresult=mycursor.fetchall()
 mydb.commit()
 for i in myresult:
     dosomething=0
 for k in i:
      return(k)


def string_ParseTo_Float(mystring):
 alist=[]
 k=mystring.split("X:")
 j=k[0]

 x=j.split("ID:")
 j=x[1]
 ID=j
 m=k[1].split("Y:")
 long=m[0]
 n=m[1].split("TIME:")
 lat=n[0]
 c=n[1].split("DATE: ")
 time=c[0]
 date=c[1]

 return(ID,long,lat,time,date)


"""
with open('text_database') as f:
    content = f.readlines()
content = [x.strip() for x in content]

j=count_rows()
for i in range(1,len(content)):
 IDNumber,longitude,latitude,timeData,dateData=string_ParseTo_Float(content[i]) 
 insert_table(int(j+2),str(IDNumber),float(longitude),float(latitude),str(timeData),str(dateData))
 j=j+1

mycursor.execute('SELECT * FROM PersonsData ORDER BY IDNumber');
"""
