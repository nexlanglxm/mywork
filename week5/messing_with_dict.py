#messing with dictionaries

car = {
    "make" : "nissan",
    "model" : "350z",
    "year" : "2006",
    "owner" : {
        "name" : "neil",
        "number" : "126"
    }
}
print(car["owner"]["name"])
print(type(car["owner"].get("name")))

for key in car:
    print(key, 'has value', car[key])