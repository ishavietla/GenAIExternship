#dictionary with basic personal information
me = {
    "name": "Isha",
    "age": 21,
    "city": "Dallas"
}

# adding a new key-value pair
me["favorite color"] = "Pink"

# updating the city
me["city"] = "Austin"

# print
print("Keys:", ", ".join(me.keys()))
print("Values:", ", ".join(str(value) for value in me.values()))
