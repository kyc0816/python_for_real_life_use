import json

# (1)
print('\n(1)\n')
# 이렇게 한줄로 하는건 오케이. 근데 무조건 쌍따옴표 써야됨.
json_string = '''{"1" : 1, "2" : "2", "3" : "yo"}''' 
print('Type of json_string\n   --> ', type(json_string)) # 아직까지는 단순 string이지.

jsoned = json.loads(json_string) # string 형태로 존재하는 json을(?) 불러와서 python object로 바꿔버림
print('Type of jsoned\n   --> ', type(jsoned)) # dict
print('jsoned\n   --> ', jsoned)

# (1.5) 그렇다면 ''' 요거 없다면?
print('\n(1.5)\n')
python_object = {"1" : 1, "2" : "2", "3" : "yo"}
print('Type of python_object\n   --> ', type(python_object)) # dict

# (2) 이번엔 살짝 더 복잡 --> 내부의 데이터를 뽑아볼거임 # 밑에 쟤는 json 역할이므로 None이 아니라 null이 들어가있어야 loads 가능
print('\n(2))\n')
nested_json_string = '''
{
    "a" : 1,
    "b" : "hi",
    "c" : [
        {
            "ca" : "yo"
        },
        {
            "cb" : null
        }
    ],
    "d" : null
}
'''

nested_jsoned = json.loads(nested_json_string)
print('Type of nested_json_string\n   --> ', type(nested_jsoned)) # dict
print('nested_json_string\n   --> ', nested_jsoned)
print('You see that "null" in JSON-string is now converted into\n   --> ', nested_jsoned['d'])

print('Now this is just a Python Object, we can do this complicated job too\n   -->')
for i in nested_jsoned['c']:
    print(i)