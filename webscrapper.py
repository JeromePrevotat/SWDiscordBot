###############################################################################
#                         IMPORTS                                             #
###############################################################################

import requests

from bs4 import BeautifulSoup


def get_ablt_desc(htmlDoc, url):
        soup = BeautifulSoup(htmlDoc, 'html.parser')
        i = len(url) - 1
        while url[i] != '#':
            i -= 1
        target = url[i:]
        return soup.find('a', attrs={'data-target':target}).find('p').get_text()
