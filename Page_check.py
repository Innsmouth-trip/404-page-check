from urllib.error import HTTPError
from urllib.request import urlopen

with open('url.txt', 'r') as text_file:
    url_list = text_file.readlines()

for line in url_list:
    url = line.replace(
        'https://site.ru', 'http://test.site.ru'
    ).strip()

    print(str(url_list.index(line) + 1) + ' of ' + str(len(url_list)))
    print('---')
    print(url)

    try:
        print(urlopen(url))
            
    except HTTPError:
        with open('url_404.txt', 'a+') as results:
            results.write(url + '\n')
