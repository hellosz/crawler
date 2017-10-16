import requests

baseUrl = 'https://www.591.com.hk/home/user/doLogin';

data = {
    'user_name': 13554416610,
     'user_pwd': 'lessismore',
        'vcode': '',
    'verifycode': '',
    'cookie': 'on',
    'redirect': ''
};

session = requests.Session()
response = session.post(baseUrl, data=data, verify=False)
print(response.text)
