users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
    },
    "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"}
}

print(users["address"]["suite"])

import json
result = json.dumps(users)
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)

