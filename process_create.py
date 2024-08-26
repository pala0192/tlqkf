#!C:\Python38\python.exe

import cgi
form = cgi.FieldStorage()
title=form["title"].value
description=form["description"].value
if 'image_link' in form:
    image_link=form["image_link"].value
    
else:
    image_link=''
opened_file=open('databox/'+title,'w',encoding='utf-8')
opened_file.write(description)
opened_file.close()

opened_file=open('databox_image/'+title,'w',encoding='utf-8')
opened_file.write(image_link)
opened_file.close()


print("Location: index.py")
print()
