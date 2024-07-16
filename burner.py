# Užduotys apie Dictionaries
# Sukurti ir atspausdinti žodyną:
# Sukurkite žodyną su šiais poromis: {'name': 'Alice', 'age': 30, 'city': 'Vilnius'}
my_dict = {"name": "Alice", "age": 30, "city": "Vilnius"}


# Atspausdinkite visą žodyną.
print(my_dict)
# Pasiekti ir pakeisti reikšmes:
# Naudodami aukščiau sukurtą žodyną, atspausdinkite reikšmę, susijusią su raktu 'name'.
print(my_dict.get("age"))
# Pakeiskite reikšmę, susijusią su raktu 'age', į 31.
my_dict["age"] = 31
print(my_dict)
# Atspausdinkite modifikuotą žodyną.
# Žodyno metodai:

# Sukurkite žodyną: {'apple': 2, 'banana': 5, 'cherry': 7}
my_dict = {"apple": 2, "banana": 5, "cherry": 7}
# Naudokite metodą keys() ir atspausdinkite visus raktus.
raktai = my_dict.keys()
print(my_dict.keys())
print(list(raktai))
# Naudokite metodą values() ir atspausdinkite visas reikšmes.

# Naudokite metodą items() ir atspausdinkite visus raktų-reikšmių poras.
for key, value in my_dict.items():
    print(f"{key} : {value}")
# Patikrinimai ir naujų įrašų pridėjimas:

# Sukurkite tuščią žodyną.
my_dict = {}
# Pridėkite tris įrašus: 'name': 'John', 'age': 25, 'city': 'Riga'.
my_dict.update({"name": "John", "age": 25, "city": "Riga"})
print(my_dict)
# Atspausdinkite žodyną.
# Patikrinkite, ar raktas 'age' egzistuoja žodyne, ir atspausdinkite rezultatą.
print("name" in my_dict)
