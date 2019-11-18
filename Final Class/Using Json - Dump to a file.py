import json as myjson

product =[
    {
        "toothpaste":"Close-up",
        "price":1230,
        "quantity":500
    },

    {
        "toothpaste": "Flourish",
        "price": 2340,
        "quantity": 700
    },

    {
        "toothpaste": "Dabur",
        "price": 700,
        "quantity": 1500
    },

    {
        "toothpaste": "Pepsodent",
        "price": 2230,
        "quantity": 10000
    },

    {
        "toothpaste": "Maclene",
        "price": 2430,
        "quantity": 900
    },




]

jsonprods = myjson.dumps(product)

print("The Product List is ")
print(jsonprods)

with open("prodlist.json","w") as myjsfile:
    jsonprodlist = myjson.dump(jsonprods,myjsfile)
print(jsonprodlist)