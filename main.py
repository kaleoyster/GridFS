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

inputDir = 'DCHUB_1'          #Input directory, containing subfolders and files to be imported in MongoDB
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
    folders = {}
    FileType = {}
    cases = {}
    D = {}           # Dictionary, containing mapping of caseId and Structure Number
    createMap(D) 
    print(D['334824132'])  # creates a Map
    FileCounter = 0        # counter for total number of files
    ExtentionArr = []      # Array for storing extention
    CaseArr = []           # Array for storing extention
    folderArr = []  
 
    for root, dirs, files in os.walk(inputDir):
        level = root.replace(inputDir,' ').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent,os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}[+] Importing...{} '.format(subindent,f)) 
            FileCounter = FileCounter + 1
            fullpath = os.path.join(root,f)
            pathList = fullpath.split(os.sep) 
            _, caseId , folderType, fileName = pathList #unpacking of pathList
            filePrefix, fileExtention = splittext(fileName)
            folderName = caseId+' '+folderType
            ExtentionArr.append(fileExtention)
            CaseArr.append(caseId)
            folderArr.append(folderName)
            case = str(caseId)
            #print(case)
            structureNumber = D[case]
            #print("Structure Number : ", structureNumber)
            data = open(fullpath,'rb')
            thedata = data.read()   
            stored = fs.put(thedata,
                            fileName=fileName,             #example: "fileName":"C000101215-2008-024.JPG"
                            caseId = caseId,               #example: 'caseId':'333380240'
                            folderType=folderType,         #example: 'folderType':'drawings'    
                            structureNumber=structureNumber                                   
                            ) 
           #prints full path of file which is imported in MongoDB
    print("Total file Stored: ", FileCounter)              #prints total count of file imported in MongoDB    
    ##
    extKey = Counter(ExtentionArr).keys()                  #returns dict, Unique file extentions present in files   eg: ('pdf','tif')
    extValue = Counter(ExtentionArr).values()              #returns dict, Count of file extention present in files  eg: ( 2, 2)

    for k, v in zip(extKey,extValue):                      #Zipping extention dictionary and Value dictionary together
        FileType[k] = v           
    
    for extKey, extValue in FileType.items():              # printing extKey and their count
        print(extKey[1:],': ', extValue)
    ##
    caseKey =   Counter(CaseArr).keys()                    # returns dict, Unique file extentions present in files   eg: ('pdf','tif')
    caseValue = Counter(CaseArr).values()                  # returns dict, Count of file extention present in files  eg: ( 2, 2)
    for k, v in zip(caseKey,caseValue):                    # Zipping extention dictionary and Value dictionary together
        cases[k] = v           
    
    for caseKey, caseValue in cases.items():               # printing extKey and their count
        print(caseKey[1:],': ', caseValue)
    ##
    folderKey =   Counter(folderArr).keys()                #returns dict, Unique file extentions present in files   eg: ('pdf','tif')
    folderValue = Counter(folderArr).values()              #returns dict, Count of file extention present in files  eg: ( 2, 2) 
    for k, v in zip(folderKey,folderValue):                # Zipping extention dictionary and Value dictionary together
        folders[k] = v        
    
    for folderKey, folderValue in folders.items():         # printing extKey and their count
        print(folderKey[1:],': ', folderValue)

	
    ##
   

#Main function
if __name__ == "__main__":
  startTime = time.time()
  main()
  endTime = time.time()
  print(" Time Taken :",(endTime - startTime))
