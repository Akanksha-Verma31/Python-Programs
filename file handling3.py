f = open("write.txt","r")
print(f.readline(10))
# prints 10 characters
print(f.readline())
# prints first line of the file
print(f.readline())
# prints second line of the file
print(f.readline(10))
f.close()