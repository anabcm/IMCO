import json
import csv
import numpy as np
 

def para_dic(dictionary,writer,lista_todo,keys_todo):
    #print keys_todo
    for i in dictionary.values():
        if type(i) is list:#                                
            #para_lista(i,writer,lista_todo,keys_todo)
                                 #print r
            keys_todo=list(set(keys_todo+para_lista(i,writer,lista_todo,keys_todo)))
        if type(i) is unicode:
            
            writer.writerow([i])
            lista_todo.append(i)
                                 
        if type(i) is dict:                              
            writer.writerow(i.keys())
            keys_todo=keys_todo+list(i.keys())
            keys_todo=list(set(keys_todo+para_dic(i,writer,lista_todo,keys_todo)))
            #keys_todo=list(set(keys_todo+i.keys()))
            #print keys_todo
            #para_dic(i,writer,lista_todo,keys_todo)
    return keys_todo
        
                              
                                                   
def para_lista(lista,writer,lista_todo,keys_todo):
    #print keys_todo
    
    for r in lista:

        if type(r) is list:#                                
            #para_lista(r,writer,lista_todo,keys_todo)
                                 #print r
            keys_todo=list(set(keys_todo+para_lista(r,writer,lista_todo,keys_todo)))
        if type(r) is unicode:
            writer.writerow([r])
            lista_todo.append(r)
                                 
        if type(r) is dict:                              
            writer.writerow(r.keys())
            keys_todo=keys_todo+list(r.keys())
            keys_todo=list(set(keys_todo+para_dic(r,writer,lista_todo,keys_todo)))
    return keys_todo


name='/home/anabcm/NetBeansProjects/IMCO/src/aja.json'
salida=open("/home/anabcm/NetBeansProjects/IMCO/src/contratos.csv","w")
salida_todo=open("/home/anabcm/NetBeansProjects/IMCO/src/contratos_2.csv","w")
lista_todo=[]
keys_todo=[]
string=""
with open(name, 'r') as f:
    read_data = f.read()
    string=string+read_data
d = json.loads(string)

writer=csv.writer(salida)
writert=csv.writer(salida_todo)
for row in d:
    writer.writerow(row.keys())
    items=row.keys()
    keys_todo=list(set(keys_todo+row.keys()))
    for i in row.values():
        print type(i)       
        if type(i) is dict:
            writer.writerow(i.keys())
            keys_todo=list(set(keys_todo+i.keys()))
            #print keys_todo
            keys_todo=list(set(keys_todo+para_dic(i,writer,lista_todo,keys_todo)))
        if type(i)is list:
            keys_todo=list(set(keys_todo+para_lista(i,writer,lista_todo,keys_todo)))
        if type(i) is unicode:
            writer.writerow([i])
            lista_todo.append(i)
    writert.writerow(lista_todo)    
    lista_todo=[]
    writer.writerow(["========================================"])
writert.writerow(list(set(keys_todo)))
print list(set(keys_todo))





