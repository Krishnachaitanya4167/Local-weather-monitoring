import MySQLdb
##declaring 4 lists to store the retrieved values
xsh=[]##for values of humidity
xsti=[]##for timestamp of values of humidity
yst=[]##for  values of temperature
ysti=[]##for timestamp of values of temperature


db=MySQLdb.connect(host="localhost",user="root",passwd="****",db="****")##connecting to database
cursor=db.cursor()


sql = "SELECT * FROM data where attribute='hum'&& device='name of the device'" ##command to retrieve values from database w.r.t device name and attribute humidity
cursor.execute(sql)
results = cursor.fetchall() 
for row in results:
     xsh.append(row[2])  ##retrieved humidity value stored in list xsh
     xsti.append(row[3]) ##retrieved time stamp of humidity value stored in list xsti

    
sql = "SELECT * FROM data where attribute='tem'&& device='name of the device'"##command to retrieve values from database w.r.t device name and attribute temperature
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
     yst.append(row[2]) ##retrieved temperature value stored in list yst
     ysti.append(row[3]) ##retrieved time stamp of temperature value stored in list ysti
    


