from Liga import *

dic_liga=dict()
liam = Liga("liga","Arg")
dic_liga['Arg'] = liam

print("Ligas:")
for key in dic_liga.keys():
    print(key,"--->",dic_liga.get(key).nombre)

dic_liga.pop("Arg")

print("Ligas:")
for key in dic_liga.keys():
    print(key,"--->",dic_liga.get(key).nombre)
