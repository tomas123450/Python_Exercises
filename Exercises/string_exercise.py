# slicing string/formating string

# len(string)
string = "Bananai auga aukstai"
len(string)

# str(7) pavers i stringa

# count
print(string.count("an", 0, 10))  # 2

# split jei norim kad ne ant tarpu splitintu (",")
string = " ' 7 77 7 7 Hello world banana"
print(string.split())  # ["Hello","world"]
print(string.strip(" 7'"))

# replace
print(string.replace("Hello", "Goodbye"))

### STRING SLICING
string = "123456789101112"
print(string[1:5:2])
print(string[0 : string.index("5")])


###String formating
print(string + string + "Hello world")
print("Welcome to {0} i hope you feeling good {1}".format("Shop", "Tom"))
print(
    "Welcome to {shop} i hope you feeling good {name}".format(
        shop="Akropolis", name="Tom"
    )
)

listas = [1, 2, 3, 4, 5, 6, 6]
new_list = listas.copy()
print(listas.count(6))
new_list[0] = 0
print(listas)

my_dict = {"labas": "Florida"}
print(my_dict.get("labas"))

### Ko nezinojau ISMOKT ENUMERATE(), del
dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])

{x: x**2 for x in (2, 4, 6)}

knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)


questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
print(list(zip(questions, answers)))

class Fruits:
    def __init__(self) -> None:
        pass
    def print_fruits():
        
