# tell function
f = open("write2.txt","r+")
print(f.tell())
f.write("\n My name is khan.")
print(f.tell())
f.close()
f = open("write2.txt","a")
print(f.tell())
f.close()