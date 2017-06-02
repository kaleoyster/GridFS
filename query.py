'''
python version: 3.x
Program description: Import DataCenter files in MongoDB using gridFS

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
client = MongoClient()        #creation of MongoClient
db = client.DCHUB             #contects to database in MongoDB
fs = gridfs.GridFS(db)        #Creation of instance of GridFS
print("Connected..")

# Global variables, required for query
results = []
	
# returns filename, extention from file name
def getData(query):
    dataArr = []
    for gridOut in fs.find(query):
        data = gridOut
        dataArr.append(data)
    return dataArr

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
    results = getData(query)
    print(results)

#Main function
if __name__ == "__main__":
  startTime = time.time()
  main()
  endTime = time.time()
  print(" Time taken :", (endTime - startTime))


