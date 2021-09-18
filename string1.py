import string
str1 = "apple guava"
str2 = "10"
str3 = " "
print(len(str1))
print(str1.find("p"))    # if element present it will return index
print(str1.find("z"))   # otherwise it will return -1
print(str1.find("p",2))
print(str1.find("p",3,6))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.isupper())
print(str1.islower())
print(str3.isspace())
print(str2.isdigit())
