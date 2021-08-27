x= ["apple","banana"]
y= ["apple","banana"]
z=x
print(x is not y)    # both lists are stored at diff locations
print(x is not z)    # they are stored at same locations, also id's are same here
print(x[0] is y[0])
id(x)
id(y)
id(z)
