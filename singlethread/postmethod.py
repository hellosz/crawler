import requests
#请求url

url = 'https://www.crowdfunder.com'
data = {'q' : 'filter', 'page' : 2}

response = requests.post(url, data=data)
response.encoding = 'utf-8'
print(response.text)
