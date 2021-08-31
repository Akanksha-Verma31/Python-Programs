# Reading a text file
f = open("write.txt","r")     # f returns a file pointer
content = f.read()
print(content)
f.close()