# coding=utf-8
#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup


def getSoupLinks(page, pages_poems, links_pages):
    html_doc = urllib.request.urlopen(page).read()
    soup = BeautifulSoup(html_doc, "lxml")
    data1 = pages_poems.copy()
    data2 = links_pages.copy()
    for link in soup.find_all('a'):
        if(link.get('class')):
            if ('poemlink' in link.get('class')):
                data1.add(domen+link.get('href'))
        if('/avtor/dimagav' in link.get('href')):
            data2.add(domen+link.get('href'))
    return [data1, data2]


pages_poems = set()
links_pages = set()
domen = 'https://www.stihi.ru'
author = 'dimagav'
page = domen+'/avtor/'+author
pages_poems, links_pages = getSoupLinks(page, pages_poems, links_pages)


for page in links_pages:
    pages_poems, links_pages = getSoupLinks(
        page, pages_poems, links_pages)

# big_data = []

pages_poems = list(sorted(pages_poems))
for poem in sorted(pages_poems):
    html_doc = urllib.request.urlopen(poem).read()
    soup = BeautifulSoup(html_doc, "lxml")
    title = str(soup.find_all('h1')[0])
    text = str(soup.find_all('div', 'text')[0])
    # big_data.append([poem, title, text])
    file = './poems/'+poem[21:-4].replace('/', '.')+'_'+title[4:-5]+'.txt'
    f = open(file, 'w', encoding="utf-8")
    f.write(text[18:-6])
    # break

print('end')
