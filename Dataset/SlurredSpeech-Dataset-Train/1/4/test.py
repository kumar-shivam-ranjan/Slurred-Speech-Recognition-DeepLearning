
import os


L=[]
for count, filename in enumerate(os.listdir("E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\4")):
    path="1-4-0"
    if(filename.endswith('.flac')==False):
        continue
    index=filename.index('.flac')
    L.append(filename[:index])
print(L)
#     newname=filename[:index]
#     L.append(newname+"\n")
#     if len(newname)==1:
#         path=path+"00"+newname+".flac"
#     elif len(newname)==2:
#         path=path+"0"+newname+".flac"
    
#     print(filename,path)
#     filename="E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\4\\"+filename
#     path="E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\4\\"+path
#     os.rename(filename,path)



# f=open("E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\4\\1-4.trans.txt","r")
# L=f.readlines()
# print(L)
# ans=[]
# for i in L:
#     ans.append(i.upper())
# print(ans)

# f=open("E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\4\\1-4.trans.txt","w")
# f.writelines(ans)


      



