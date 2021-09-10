# pattern 1 with user input
n = int(input("Enter the range: "))
for row in range(0,n):
    number = 1;
    for column in range(0,row+1):
        print(number,end=" ")
        number = number +1
    print("\r")
