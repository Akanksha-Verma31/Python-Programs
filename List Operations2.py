# list is mutable(we can modify) (add,update,delete)
a = ['a','b','c','d','e']
# update
a[0] = 'f'
print(a)
# update number of elements in one go
a[:3] = ['x','y']
print(a)
# add elemets in the list
b = [1,2,3]
b[1:1] = [5]
print(b)
c = [1,2,3,4]
c[2:2] = [5,6]
print(c)
# delete elements from the list
a = ['a','b','c']
a[1:3] = []
print(a)
