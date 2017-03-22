File1:cb2

     In this file there are 3 functions readfile,timestamp,inser which are used to read lastline from a file,
     creating timestamp ,inserting the data into database respectively.
     
File:main
     
      This file imports the functions present in cb2 by name kc and uses them to insert the recieved sensor values
      (i.e the redirected output from mqtt console to a text file)  into database.
      
 File:ddd
 
      This file is used to retrieve the data base and stores them into lists which can be used for further data processing as per 
      required application.
