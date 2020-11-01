import requests
# import pdb
url = 'http://127.0.0.1:5000/query?q=home&p=5'
response = requests.get(url)
result = response.json()
print(result)
