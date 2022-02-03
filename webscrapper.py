###############################################################################
#                         IMPORTS                                             #
###############################################################################

import requests

from bs4 import BeautifulSoup


def get_html_doc(search, category, baseUrl):
    htmlDoc = None
    if category == 'img' and search != '':
        search = search.split(' ')
        search = [s.capitalize() for s in search]
        search = '_'.join(search)
        htmlDoc = requests.request('GET',
            baseUrl + '/wiki/' + search)
        if htmlDoc.status_code == 200:
            return htmlDoc.content
    if category == 'ability':
        htmlDoc = requests.request('GET', 'https:' + baseUrl)
        if htmlDoc.status_code == 200:
            return htmlDoc.content

def get_ablt_desc(htmlDoc, url):
        soup = BeautifulSoup(htmlDoc, 'html.parser')
        i = len(url) - 1
        while url[i] != '#':
            i -= 1
        target = url[i:]
        return soup.find('a', attrs={'data-target':target}).find('p').get_text()

def get_ablt_img(effect):
    baseUrl = 'https://wiki.swgoh.help'
    htmlDoc = None
    img = None
    if effect != '':
        htmlDoc = get_html_doc(effect, 'img', baseUrl)
    if htmlDoc is not None:
        soup = BeautifulSoup(htmlDoc, 'html.parser')
        img = soup.find('table', class_='wikitable').find('img')
        img = baseUrl + img['src']
    return img
