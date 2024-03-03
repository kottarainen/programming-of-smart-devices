import json

x = '{ "firstName": "tester", "lastName": "tester", "city": "Vilnius"}'

y=json.loads(x)

print (y["firstName"])

y["firstName"] = "Jane"
y["lastName"] = "Doe"
y["Age"] = 20

new_json = json.dumps(y) #convert the dictionary to json

print(new_json)
