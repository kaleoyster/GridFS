from pymongo import MongoClient
import gridfs
import os
import base64


target = 'DCHUB' 
client = MongoClient()
client.drop_database("DCHUB")
db = client.DCHUB
fs = gridfs.GridFS(db)


def splittext(fname):
    filename, extention = os.path.splitext(fname)
    return filename , extention 


def main():
    count = 0      
    for root, dirs, files in os.walk(target):
        for f in files:
            count = count + 1
            fullpath = os.path.join(root,f)
            pathList = fullpath.split(os.sep)
            _, caseId , folderType, fileName = pathList
            filePrefix, fileExtention = splittext(fileName)
            data = open(fullpath,'rb')
            thedata = data.read()
            stored = fs.put(thedata,filename=fileName , path = { "caseId": caseId,
                                                                      
                                                                "folderType": folderType,
                                                             
                                                                "fileName": fileName

                                                             }, caseId = caseId, folderType=folderType,  fileName=fileName)
            
            print('[ + ] Storing ..'+ fullpath +'')
            print('extention:', fileExtention)
    print("Total file Stored: ", count)   
   # print(fs.list())  

if __name__ == "__main__":
  main()
'''
count = 0 
for grid_out in fs.find({'caseId':'333380240','folderType':'drawings'}):
    data = grid_out
    count = count + 1
print("Total files Stored : ", count) 
'''
