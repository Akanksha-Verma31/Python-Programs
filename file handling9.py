f = open("write2.txt","r")
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
f.close()