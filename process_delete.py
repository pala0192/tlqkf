#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('databox/'+pageId)

print("Location: index.py")
print()
