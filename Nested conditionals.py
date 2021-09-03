# NESTED CONDITIONALS

x = int(input("Enter a Number : "))
if x>=0 :
    print(x," is greater than 0")
    print("if block")
    if  x == 0 :
        print(x," is equal to 0")
        print("Nested if..")
else:
    print(x," is lesser than 0")
    print("Else block..")
    
print("Outside of nested conditionals...")
