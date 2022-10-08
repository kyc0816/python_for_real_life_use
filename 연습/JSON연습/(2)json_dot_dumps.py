import json

# (1)
print('\n(1)\n')
# json.dumps는 json.loads의 반대. 즉 python object를 json string으로 만들어준다.
python_object = {"a" : 1, "b" : "hi", "c" : [{"ca" : "yo"}, {"cb" : None}], "d" : None}
dumped = json.dumps(python_object, indent=2) # dumps는 이렇게 indent 지정 가능
print('Type of dumped\n   --> ', type(dumped))
print('dumped\n   --> ', dumped)

with open ('new_json.json', 'w') as f:
    dumped2 = json.dump(python_object, f, indent=2) # dumps는 이렇게 indent 지정 가능
print('Type of dumped\n   --> ', type(dumped2))
print('dumped\n   --> ', dumped2)