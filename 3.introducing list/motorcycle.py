motorcycle = ["hoda", "yamaha", "suzuki"]
print(motorcycle)


# replace method
""" motorcycle[1] = "ducati"
print(motorcycle) """


# append method
""" motorcycle.append("royal enfield")
print(motorcycle)

bike = []
bike.append("splendor")
bike.append("bullet")
bike.append("gt650")

print(bike) """

# insert method
""" motorcycle.insert(0, "ducati")
print(motorcycle)

motorcycle.insert(2, "bullet")
print(motorcycle) """


# removing item form list

""" del motorcycle[1]
print(motorcycle)

del motorcycle[1]
print(motorcycle) """


# pop method

""" popped_motorcycle = motorcycle.pop()
popped_motorcycle = motorcycle.pop(1)
print(popped_motorcycle)
print(motorcycle)

name = {
    "name": "Krish",
    "age": 20,
    "city": "jetpur"
}
remove_age = name.pop("age")
print(name)

city = name.pop("city")
print(f"I am living in the {city.title()} city") """




# removing an item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles.remove('suzuki')
# print(motorcycles)

not_buy = 'suzuki'
motorcycles.remove(not_buy)
print(motorcycles)
print(f"I dont like {not_buy.title()} bikes")
