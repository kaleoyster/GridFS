'''
python version: 3.x
Program description: contains createQuery function which creates a custom query.
Author: Akshay Kale
'''
#!/usr/bin/python
#importing Abstract Syntax Trees
import ast

#return a valid query, depending on values available.
def createQuery(caseId, folderType, fileName):
    D = {   
         "caseId":caseId,
         "folderType":folderType,
         "fileName":fileName
        }

    query = ''
    for k,v in D.items():
        if D[k] is '':
           pass
        else:
           form = ','+'"'+ k + '"' +':' + '"' + v + '"'
           query = query + form
    query = query[1:]
    query = '{'+ query + '}'
    query = ast.literal_eval(query)
    return query

