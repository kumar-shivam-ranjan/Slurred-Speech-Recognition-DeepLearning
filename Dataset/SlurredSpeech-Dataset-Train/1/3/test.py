
# import os


# L=[]
# for count, filename in enumerate(os.listdir("E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\3")):
    
#     if(filename.endswith('.flac')==False):
#         continue
#     print(filename)
#     index=filename.index('.flac')
#     L.append(filename[:index]+"\n")

f=open("E:\\Slurred-Speech-Recognition-DeepLearning\\Dataset\\SlurredSpeech-Dataset-Train\\1\\3\\1-3.trans.txt","r")
L=f.readlines()
# print(L)
ans=[]
for i in L:
    ans.append(i.upper())
f=[]
for i in ans:
    f.append(i[:8])

print(f)


      



