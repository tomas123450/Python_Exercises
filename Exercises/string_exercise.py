# len(string)
string = "Bananai auga aukstai"
len(string)

#str(7) pavers i stringa

#count
print(string.count("an",0,10)) # 2 

#split jei norim kad ne ant tarpu splitintu (",")
string = " ' 7 77 7 7 Hello world banana"
print(string.split()) #["Hello","world"] 
print(string.strip(" 7'"))

#replace
print(string.replace("Hello", "Goodbye")) 

### STRING SLICING
string = "123456789101112"
print(string[1:5:2])
print(string[0:string.index("5")])


