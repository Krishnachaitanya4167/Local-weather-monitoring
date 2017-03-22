import datetime
import time
import MySQLdb

def read_file():
   f=open('/home/krishna/payload.txt',"r") ##opening the file in read mode
   lineList=f.readlines()   ##reading all the lines in the file
   f.close()
   k=str(lineList[-1])   ##considering the last line from the list of read lines.
   parts=k.split(" ")     ##splits the string(lastline) with respective to space and stores in list named parts
   device=parts[0]
   attribute=parts[1]
   value=parts[2]
   return (device,attribute,value)   ##returns these 3 attributes as output of function read_file

def time_stamp():
    ts = time.time()    ##gives unformatted timestamp
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')  ##converts the unformatted timestamp to user understandable format
    return st   ##output of function time_stamp
def inser(a,b,c,d):
    db=MySQLdb.connect(host="localhost",user="root",passwd="*****",db="****") ##connecting to database
    cursor=db.cursor()
    query = "INSERT INTO data (device,attribute,value,timestamp) VALUES(%s,%s,%s,%s)" ##query for insertion of required attributes
    args = (a,b,c,d)  ##a,b,c,d are the arguments from main.py file that are to be inserted into database
    cursor.execute(query, args)
    ## cursor.execute("""INSERT INTO SENSOR VALUES (%s,%f,%s)""",(a,b,c))
    db.commit()    ##save  the changes done to the database.
    db.close()
    return
