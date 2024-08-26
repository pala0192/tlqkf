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
    listStr = ''
    for item in file:
        listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)
    return listStr

form = cgi.FieldStorage()
if  'id' in form:
    pageId = form["id"].value
    description = open('databox/'+pageId, 'r',encoding='utf-8').read()

else : 
    pageId = 'Hanmin Wiki'
    description = 'Thank you for using our website'


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
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" style="width:90%; font-size:280%" placeholder="name">
        </p>
        <p><textarea rows="2" name="description"
        style="width:90%; font-size:280%" placeholder="description"></textarea></p>
        <p><textarea row="20" name="image_link" style="width:90%; font-size:60%; height=70px" placeholder="image_link"></textarea></p>
        <p><input type="submit"  style="width:90%; font-size:280%"></p>
    </form>
    
    <div style="border:black solid 1px; padding:3%">
        <h3 style="font-size:300%;">contents</h3>
        <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
</body>
</html>
    '''.format(title=pageId, desc= description, listStr=getList()))
            