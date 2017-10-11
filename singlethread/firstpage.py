import requests
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html.encoding = 'utf-8'
print(html.text)
