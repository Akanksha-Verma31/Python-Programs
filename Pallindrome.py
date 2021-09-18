# palindrome
str = input("string: ")
mid = len(str)//2
if len(str)% 2 == 0:
    s1 = str[:mid]
    s2 = str[mid:]
else:
    s1 = str[:mid]
    s2 = str[mid+1:]

if s1 == s2[::-1]:
    print("palindrome")
else:
    print("not palindrome")
