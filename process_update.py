#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form["description"].value

# if 'image_link' in form:
#     image_link=form["image_link"].value
    
# else:
#     image_link=''
    
opened_file=open('databox/'+title,'w',encoding='utf-8')
opened_file.write(description)
opened_file.close()
os.rename('databox/'+pageId, 'databox/'+title)


    
# opened_imgfile=open('databox_image/'+title,'w')
# opened_imgfile.write(image_link)
# opened_imgfile.close()
# if os.path.isfile('databox_image/{}'.format(pageId)) :
#     os.rename('databox_image/'+pageId, 'databox/'+title)


print("Location: index.py")
print()
