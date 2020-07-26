import psycopg2
import yaml
import os

curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, 'config.yml')
f = open(yamlPath, 'r', encoding='utf-8')
ymlData = f.read()
f.close()
data = yaml.safe_load(ymlData)
conn = psycopg2.connect(**data.get('database'))
cur = conn.cursor()
