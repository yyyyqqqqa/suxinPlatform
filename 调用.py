import requests, json

# pfsm0001
# param = {'id': 'pf', 'login_id': '200114029-46c5-8efc-868f564bdd05'}

# pfsm0002
param = {'sys_id': 'pf', 'module_id': 'sm',
         'name':'测试模块',
         'login_id': '200114029-46c5-8efc-868f564bdd05'}
param['in_param'] = '''{"login_id":[">0","str"],"sys_id":[">0","str"],"module_id": ["==2", "str"], "name": [">6", "str"],"in_param": [">6", "str"],"out_param": [">0", "str"],"note": ["==0", "str"]}'''
param['out_param'] = '''{"error":"值为0:表示注册成功,其他都是错误"}'''

r = requests.post("http://127.0.0.1:5000/pfsm0002.do", json=param)
a = json.loads(r.text)

print(a)