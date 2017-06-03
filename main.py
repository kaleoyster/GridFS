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
from collections import Counter


#importing python files 
from map import createMap, searchStruct

inputDir = 'DCHUB'           #Input directory, containing subfolders and files to be imported in MongoDB
client = MongoClient()        #creation of MongoClient
client.drop_database("DCHUB") #Delete already exisiting database
db = client.DCHUB             #Create new database in MongoDB
fs = gridfs.GridFS(db)        #Creation of instance of GridFS

# returns filename, extention from file name
def splittext(fname):
    filename, extention = os.path.splitext(fname)
    return filename , extention 

#Driver function
def main():
    #FileType = {}
    D = {}           # Dictionary, containing mapping of caseId and Structure Number
    createMap(D)     # creates a Map
   # print(D) 
   # print("structureNumber for case ID: ",D['334824132'])
    FileCounter = 0        # counter for total number of files
    ExtentionArr = []      #    
    for root, dirs, files in os.walk(inputDir):
        for f in files:
            FileCount = FileCounter + 1
            fullpath = os.path.join(root,f)
            pathList = fullpath.split(os.sep) 
            _, caseId , folderType, fileName = pathList #unpacking of pathList
            filePrefix, fileExtention = splittext(fileName)
            ExtentionArr.append(fileExtention)
            case = str(caseId)
            #print(case)
            structureNumber = D[case]
            print("Structure Number : ", structureNumber)
            data = open(fullpath,'rb')
            thedata = data.read()   
            stored = fs.put(thedata,
                            fileName=fileName,              #example: "fileName":"C000101215-2008-024.JPG"
                            caseId = caseId,                #example: 'caseId':'333380240'
                            folderType=folderType,          #example: 'folderType':'drawings'    
                            structureNumber=structureNumber                                   
                            ) 
            print('[ + ] Storing ..'+ fullpath +'') #prints full path of file which is imported in MongoDB
    print("Total file Stored: ", FileCounter)             #prints total count of file imported in MongoDB
    #print("FileExtenion: ", ExtentionArr)     
    #k = Counter(ExtentionArr).keys()
    #v = Counter(ExtentionArr).values()
    #for a,b in zip(k,v):
    #    FileType[a] = b
    
    #print(FileType)
#Main function
if __name__ == "__main__":
  startTime = time.time()
  main()
  endTime = time.time()
  print(" Time Elasped :",(endTime - startTime))
