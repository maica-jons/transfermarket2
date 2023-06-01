from Liga import *

dic_liga=dict()
liam = Liga("liga","Arg")
dic_liga['Arg'] = liam

for key in dic_liga.keys():
    print(key,"--->",dic_liga.get(key).nombre)