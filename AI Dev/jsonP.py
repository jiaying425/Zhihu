a ={
"employees":[
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
]
}

print(a)

###json.dumps : python ->json 

import json

data ={"name":"Alice",
       "age":25,
       "hobbies":["reading","swimming","traveling"]}

json_str = json.dumps(data)
print(json_str)
print('------------------------------')
print(type(json_str))

###: json->python 
json_str ='{"name": "Alice", "age": 25, "hobbies": ["reading", "swimming", "traveling"]}'
print(type(json_str))
data = json.loads(json_str)
print(data)

