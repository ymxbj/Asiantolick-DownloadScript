import requests
from selenium import webdriver
import time

url_path = 'download_url.txt'
url_lines = open(url_path, 'r').readlines()

output_file = open('image_url.txt',mode='a')

for i, line in enumerate(url_lines):
    if i < 0:
        continue
    url = line[:-1]
    response = requests.get(url)
    response = response.text
    name = response.split('display:block;">')[1]
    name = name.split('</h1><br>')[0]
    imgs_url = response.split('https://asiantolick.com/post')[1]
    imgs_url = imgs_url.split('"')[0]
    imgs_url = 'https://asiantolick.com/post' + imgs_url
    output_file.write(imgs_url + ' ' + name +'\n')
    print(i, imgs_url)

output_file.close()
