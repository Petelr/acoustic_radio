def getSize(file_obj):
    file_obj.seek(0,2)
    size = file_obj.tell()
    return size

file = open('dialtone.py', 'rb')
print getSize(file)