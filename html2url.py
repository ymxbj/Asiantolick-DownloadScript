import os
import requests

path = 'html.txt'
file = open(path,'r')
html = file.read()
file.close()
contents = html.split('href="')
output_file = open('download_url.txt',mode='a')
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
for index, content in enumerate(contents[1:]):
    url = content.split('"')[0]
    response = requests.get(url)
    response = response.text
    download_url = response.split('<b>Download:</b> <a href="')[1]
    download_url = download_url.split('"')[0]
    output_file.write(download_url+'\n')
    print(index, download_url)

output_file.close()
