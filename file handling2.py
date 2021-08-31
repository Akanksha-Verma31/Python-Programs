f = open("write.txt","r")
content = f.read(19)    # prints only first 10 characters
print(content)
f.close()