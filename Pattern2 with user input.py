# pattern 2 using user input
n = int(input("Enter range: "))
for row in range(1,n):
    for col in range(1,n+1):
        print("*", end=" ")
    print()
