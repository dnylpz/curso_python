"""
import boto3

client = boto3.client('sts',
                      aws_access_key_id='',
                      aws_secret_access_key='')



client  = boto3.client('ec2', region_name='us-east-1',
                       aws_access_key_id='',
                       aws_secret_access_key='')

security_groups = client.describe_security_groups()

print(len(security_groups['SecurityGroups']))
"""
import requests
import sys
import json
from bs4 import BeautifulSoup

response = requests.get('https://jsonplaceholder.typicode.com/todos')

""" 
ejemplo simplificado de script de monitoreo
if response.status_code != 200:
    print("el sitio esta caido", sys.stderr )
    exit(-1)
"""
data = response.text
#print(json.loads(data)[0])

res = requests.get('https://es.wikipedia.org/wiki/Monterrey')

raw_html = res.text
parsed = BeautifulSoup(raw_html, 'html.parser')

print(parsed.find_all('table')[4])
