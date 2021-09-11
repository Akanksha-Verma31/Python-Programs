n = int(input("Enter range: "))
ch = 65
for i in range(0,n):
    for j in range(0,i+1):
        char = chr(ch)
        print(char, end=" ")
        ch = ch+1
        
    print("\r")
