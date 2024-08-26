#!C:\Python38\python.exe
import cgi,os
form = cgi.FieldStorage()
searchInput=form["searchInput"].value
if os.path.isfile('databox/{}'.format(searchInput)) :
    print("Location: index.py?id={}".format(searchInput))
    print()
else:
    print("Location: searchError.py")
    print()
