from curses import savetty
import requests
import os

url_path = 'imgs_url.txt'
url_lines = open(url_path, 'r').readlines()

start_index = 0
for index,line in enumerate(url_lines):
    if index < start_index:
        continue
    line = line[:-1]
    url = line.split(' ', 1)[0]
    name = line.split(' ', 1)[1]
    save_path = os.path.join('imgs',name)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    response = requests.get(url)
    response = response.text
    response = response.split('<div data-src="')
    count = 0
    for img_url in response[1:]:
        img_url = img_url.split('"')[0]
        img = requests.get(img_url)
        count += 1
        with open(os.path.join(save_path,f'{count}.jpg'),'wb') as file:
            file.write(img.content)
            file.close()
    print(index, name)
