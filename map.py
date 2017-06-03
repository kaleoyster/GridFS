'''
Program: map.py
this program contains all the functions related to mapping.
'''
#importing Libraries
import csv

#D = {}
#Function will create a dictornary map of caseId and StructureNumber
def createMap(D):
    with open("mapping.csv",'r') as csvfile:
         reader = csv.reader(csvfile, delimiter = ',')
         for row in reader:
             caseId = row[0]
             StructureNumber = row[2]
             D[caseId] = StructureNumber
    return D

#createMap(D)
#caseId = '334824135'


def searchStruct(caseId,D):
    structureNumber = D[caseId]
    return structureNumber
    
#print(searchStruct(caseId,D))

