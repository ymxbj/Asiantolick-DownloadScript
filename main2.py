import requests
from selenium import webdriver
import time

driver = webdriver.Chrome()

url_path = 'download_url.txt'
url_lines = open(url_path, 'r').readlines()

output_file = open('file_url.txt',mode='a')
error_file = open('error.txt',mode='w')

for i, line in enumerate(url_lines):
    url = line[:-1]
    response = requests.get(url)
    response = response.text
    name = response.split('display:block;">')[1]
    name = name.split('</h1><br>')[0]
    js='''
    xmlhttpSaveAs = new XMLHttpRequest();
    xmlhttpSaveAs.open("GET", "/ajax/download_post.php?ver=1&dir=/"+dir+"&post_id="+post_id+"&post_name="+post_name, true);
    xmlhttpSaveAs.send();
    '''
    driver.get(url)
    driver.execute_script(js)
    time.sleep(1)
    js = "return xmlhttpSaveAs.responseText;"
    file_url = driver.execute_script(js)
    string = file_url + ' ' + name
    output_file.write(string + '\n')
    print(i, string)
    if file_url == '':
        error_file.write(str(i) + '\n')

output_file.close()
error_file.close()
driver.close()
