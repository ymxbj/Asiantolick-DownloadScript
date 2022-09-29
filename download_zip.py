import requests
import os

url_path = 'file_url.txt'
url_lines = open(url_path, 'r').readlines()

error_path = 'download_error.txt'
error_file = open(error_path,mode='a')

start_index = 0
for index,line in enumerate(url_lines):
    if index < start_index:
        continue
    line = line[:-1]
    url = line.split(' ', 1)[0]
    name = line.split(' ', 1)[1]
    try:
        response = requests.get(url, stream=True)
        with open(os.path.join('zips',name+'.zip'), 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(index,line)
    except Exception as r:
        print(index, '%s' %(r))
        error_file.write(str(index) + '\n')

error_file.close()
