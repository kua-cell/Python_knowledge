import requests


url1 = "https://www.icourse163.org/"

r = requests.get(url1)
with open('icourse163.html', 'w', encoding='utf-8') as f:
    f.write(r.text)


