'''
python version: 3.x
Program description: Program allows you to query using interactive interface
Author: Akshay Kale
'''
#!/usr/bin/python
#importing library
from pymongo import MongoClient
import gridfs 
import os
import time
import base64
#importing files
from queryBuilder import createQuery

print('Connecting to MongoDB...DCHUB')
client = MongoClient()        #Creation of MongoClient
db = client.DCHUB             #Connects to database in MongoDB
fs = gridfs.GridFS(db)        #Creation of instance of GridFS
print("Connected..")

# Global variables, required for query
results = []
	
# getData takes query as input returns a list of result 
def getData(query):
    data = ''
    for gridOut in fs.find({"caseId":"334824177","folderType":"media","fileName":"C000102305P_Y11_Looking north at Bent 1.jpg"}):
        data = gridOut
        data = data.read()
        #dataArr.append(data)
    return data

#write data in file

#Driver function
def main():
    caseId = ''
    folderType = ''
    fileName = ''
    #caseId = input("Enter caseId: ")
    #folderType = input("Enter fieldType: ")
    #fileName = input("Enter fileName: ")
    query = createQuery(caseId,folderType,fileName)
    #print(getData(query))
    with open("foo.JPG","wb") as f:
        f.write(getData(query))
#Main function
if __name__ == "__main__":
  startTime = time.time()
  main()
  endTime = time.time()
  print(" Time taken :", (endTime - startTime))


