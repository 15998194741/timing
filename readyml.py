# import yaml
# import os
# # with open('./config.yml', 'r', encoding='utf-8') as f:
#     # yml_data = f.read()
#
# curPath = os.path.dirname(os.path.realpath(__file__))
# yamlPath = os.path.join(curPath,'config.yml')
# f = open(yamlPath,'r',encoding='utf-8')
# ymlData = f.read()
# f.close()
# data = yaml.safe_load(ymlData)
#
# print(data)



from pgsql import cur

sql = 'select * from one'

cur.execute(sql)
print(cur.fetchall())
