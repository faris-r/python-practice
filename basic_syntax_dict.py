users = {
    "id": 1,
    "name": "Rick Rubin",
    "username": "Morty",
    "email": "certain@april.biz",
    "address": {
        "street": "avenue street",
        "suite": "Apt 551",
        "city": "New York",
        "zip code": "974-2312"
    }
}
print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"]["street"])

print(users)
print(type(users))
print("\nConverting from dictionary to JSON")
import json
result = json.dumps(users)
print(result)
print(type(result))

with open ('result.json', 'w') as file:
    json.dump(users, file)

