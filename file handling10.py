f = open("write2.txt","r")
f.seek(10)
print(f.readline())
f.close()