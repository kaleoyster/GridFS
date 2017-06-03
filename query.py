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
    dataArr = []
    for gridOut in fs.find(query):
        data = gridOut
        dataArr.append(data)
    return dataArr

def saveFile(fileName,data):
    with open(fileName,"wb") as f:
         f.write(data)

#Driver function
def main():
    caseId = ''
    fileType = ''
    fileName = ''
    caseId = input("Enter caseId: ")
    folderType = input("Enter fieldType: ")
    fileName = input("Enter fileName: ")
    query = createQuery(caseId,folderType,fileName)
    #print(query)
    result = getData(query)
    print(results)
    f.close()

#Main function
if __name__ == "__main__":
  startTime = time.time()
  main()
  endTime = time.time()
  print(" Time taken :", (endTime - startTime))


