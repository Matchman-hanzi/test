from pathlib import Path
import os,shutil,time
with open('settings.txt') as file_set:
    settings=file_set.read()
a,b,list_=0,'',[]
for i in settings:
    a+=1
    if i=='>':
        break
for i in settings[a:]:
    a+=1
    if i=='>':
        list_type=b
        if list_type=='Whitelist':
            list_type=True
        else:
            list_type=False
        break
    else:
        b+=i
b=''
for i in settings[a:]:
    if i=='>':
        list_.append(b)
        b=''
    else:
        b+=i
list_=tuple(list_)
target=Path('F:\\')
while target.exists()==False:
    time.sleep(1)
for folder,subfolder,file in os.walk(target):
    for filename in file:
        foldername=Path(folder)/filename
        if (foldername.suffix in list_)==list_type:
            newfolder='D:\\copy\\'+folder[3:]
            newfolder=Path(newfolder)
            if newfolder.exists():
                shutil.copy(foldername,newfolder)
            else:
                os.makedirs(newfolder)
                shutil.copy(foldername,newfolder)
