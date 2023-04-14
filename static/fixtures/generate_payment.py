import json
import copy
import random
import datetime

data = [
    {"model": "payapp.transaction", "pk": 1, "fields": {
        "sender": 1, "recipient": 2, "amount": 100, "time_stamp": "2023-03-16T17:41:28+00:00"
    }
    }
]

for i in range(19):
    temp = copy.deepcopy(data[0])
    temp["pk"] = i+2
    temp["fields"]["sender"] = random.randrange(1, 11, 1)
    temp["fields"]["recipient"] = random.randrange(1, 11, 1)

    while temp["fields"]["sender"] == temp["fields"]["recipient"]:
        temp["fields"]["recipient"] = random.randrange(1, 11, 1)

    amount = random.randrange(200, 50000) / 100
    temp["fields"]["amount"] = float(amount)
    data.append(temp)


with open('payment.json', 'w') as f:
    json.dump(data, f)
