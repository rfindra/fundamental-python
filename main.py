import requests

print("hello world of python")
r = requests.get('https://google.com')
print (r.status_code)
if r.status_code == 200:
    print(r.text)