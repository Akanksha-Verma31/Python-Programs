# type() gives the data type of any variable
a = 12
print("Data Type of a : ",type(a))

b = 1234567890
print("Data Type of b : ", type(b))

c = "123"
print("Data Type of c : ",type(c))

d = "akanksha"
print("Data Type of d : ",type(d))

e = int(input("Enter any thing : "))     # it will throw error if value other than int is entered
print("Data Type of e : ",type(e))

f = (input("Enter any value : "))        # its data type is always 'str'
print("Data Type of f : ",type(f))
