import json as myjson
country ="""
{"nigeria":"abuja",
"population": "180000000",
"dateOfIndep":"Oct 1, 1960",
"president":"Buhari",
"language":{
    "west":"yoruba",
    "east":"igbo",
    "north":"hausa",
    "south":"urobo"
    }
}


"""

myng = myjson.loads(country)

print(f"The capital of Nigeria is {myng['nigeria']}")
print(f"The population is {myng['population']}")
print(f" Nigeria got his independence on  {myng['dateOfIndep']}")
print(f"The president of Nigeria is {myng['president']}")
print(f"The People of Western Nigeria speaks  {myng['language']['west']}")
print(f"The People of easterners Nigeria speaks  {myng['language']['east']}")

