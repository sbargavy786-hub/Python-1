fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)
fruits.append("grape")
print("Fruits after adding grape:", fruits)
fruits.remove("banana")
print("Fruits after removing banana:", fruits)
fruits[0] = "kiwi"
print("Fruits after changing apple to kiwi:", fruits)

vegitables = {"carrot": "orange", "spinach": "green", "potato": "brown"}
print("Vegitables:", vegitables)
vegitables["tomato"] = "red"
print("Vegitables after adding tomato:", vegitables)
del vegitables["carrot"]
print("Vegitables after removing carrot:", vegitables)
vegitables["spinach"] = "dark green"
print("Vegitables after changing spinach color:", vegitables)
