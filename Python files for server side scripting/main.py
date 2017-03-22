import cb2 as kc ##importing a file named cb2 with a variable kc where the functions of reading a file,timestamp,insertion into database are present
import time   
##starting an infinite loop
while True:
  r=kc.read_file()   ##assigning the output of function readfile(in file cb2) to a variable r 
  dev=str(r[0])       
  par=str(r[1])
  val=str(r[2])
  tim=kc.time_stamp() ##assigning the output of function timestamp(in file cb2) to a variable tim
  i=kc.inser(dev,par,val,str(tim))  ##calling function inser present in file cb2 with respective arguments. 
  time.sleep(5)
  print "0k"
