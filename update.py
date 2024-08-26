#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

file= os.listdir('databox')

def getList():
    file= os.listdir('databox')
    listStr = ''
    for item in file:
        listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)
    return listStr

form = cgi.FieldStorage()

file_list = []
for files in file:
  file_list.append(files)


file_count_num=0
file_num_and_list={}
file_keys_list = []

for file in file_list:
  file_num_and_list[file]=file_count_num
  file_keys_list.append(file)
  file_count_num=file_count_num+1
  



if  'id' in form:
    pageId = form["id"].value
    description = open('databox/'+pageId, 'r',encoding='utf-8').read()
    update_link = '<a href="update.py?id={}" style="font-size:300%">Edit the document</a>'.format(pageId)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{0}">
            <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
        </form>
    '''.format(pageId)
    file_num = file_num_and_list[pageId]
    if pageId==file_keys_list[0]:
        Previous_file_name=''
        next_file_name=file_keys_list[file_num+1]
    elif pageId==file_keys_list[-1]:
        Previous_file_name=file_keys_list[file_num-1]
        next_file_name=''
    else:
        Previous_file_name=file_keys_list[file_num-1]
        next_file_name=file_keys_list[file_num+1]
    if os.path.isfile('databox_image/{}'.format(pageId)) :
        image_link=open('databox_image/{}'.format(pageId), 'r').read()
    else: image_link=''

else : 
    pageId = 'voca'
    description = 'to the Seoul National University'
    update_link=''
    delete_action=''
    file_num = 0
    Previous_file_name=''
    next_file_name=file_keys_list[0]
    image_link=''


print('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hanmin wiki making practice</title>
    <link rel="stylesheet" href="front.css">
</head>
<body>
    <div style="margin:12%; background-color: rgb(186, 210, 218);">
        <h1 style="text-align: center;"><a href="index.py"><span style="color:rgb(87, 122, 205);font-size:280%">My English</span>
        <span style="color:rgb(139, 83, 236);font-size:260%"> vocabulary book</span></a></h1>
    </div>
    <br>
    <br>
    
    <div>
        <form action="process_update.py" method="post">
            <input type="hidden" name="pageId" value="{form_default_title}">
            <p><input type="text" name="title" style="width:90%; font-size:280%" placeholder="name" value="{form_default_title}">
            </p>
            <p><textarea rows="3" style="width:90%; font-size:280%" name="description"
            placeholder="description">{form_default_description}</textarea></p>
            <p><input type="submit" style="width:90%; height:60px; font-size:280%"></p>
        </form>
    </div>
    
    <div style="border:black solid 1px; padding:3%">
        <h3 style="font-size:300%;">contents</h3>
        <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    
    <div>
        <h4 style="font-size:200%">Wanna make a document? click here</h4>
        <a href="create.py" style="font-size:300%">create your document</a>
        <br>
    </div>
</body>
</html>
    '''.format(listStr=getList(), form_default_title=pageId, form_default_description=description))
# <p><textarea row="20" name="image_link" style="width:90%; font-size:60%; height=70px" placeholder="image_link">{image_link}</textarea></p>
