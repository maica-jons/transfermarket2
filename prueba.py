from Usuario import *

dic_usu=dict()
liam = Usuario("limson","1234","liam","mac gaw",44447670,"lmg")
dic_usu['limson'] = liam

print("usuarios:")
for key in dic_usu.keys():
    print(key,"--->",dic_usu.get(key).nom_usuario)

