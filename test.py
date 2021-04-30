###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import servers_locals

if __name__ == '__main__':
    #client = swgohgg.Swgohgg()
    #charList = client.get_from_api('characters')

    class Test():
        def __init__(self):
            self.d = {
                'a':1,
                'b':2,
                'c':3,
            }

        def update_d(self):
            self.d['b']=5

        def print_d(self):
            self.update_d()
            print(self.d)

    t = Test()
    t.print_d()
