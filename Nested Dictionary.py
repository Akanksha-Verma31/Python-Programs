# nested dictionaries
# more about dictionaries
b = {"One":"Mon","Two":"Tue","Three":{"A":"Wed","B":"Thurs"},"Four":"Fri"}
print(b["Two"])
print(b["Three"]["A"])
print(b["Three"]["B"])
b["Six"] = "Sun"     # adding new element
print(b)
b = {"Five":"Sat"}
print(b)    #it will change the whole elements of dict to the new ones added
del(b["Five"])
print("Deleted dict : ",b)
b = {"One":"Mon","Two":"Tue","Three":{"A":"Wed","B":"Thurs"},"Four":"Fri"}
b.update({"One":"Holiday"})
print("Updated dict: ",b)
print(b.keys())
