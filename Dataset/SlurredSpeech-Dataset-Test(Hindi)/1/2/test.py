import os
f=open("E:\\Dataset Hindi\\1\\2\\1-2.trans.txt")
L=f.readlines()

newL=[]
for i in L:
   newL.append(i.upper())

print(newL)
f=open("E:\\Dataset Hindi\\1\\2\\1-2.trans.txt","w")
f.writelines(newL)
f.close()
    


