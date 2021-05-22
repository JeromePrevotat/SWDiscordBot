###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import requests

import swgohgg

import servers_locals

if __name__ == '__main__':
    LEADS = ['Leader: +Counter', 'Leader: +Critical Avoid',
	'Leader: +Critical Chance', 'Leader: +Critical Damage',
	'Leader: +Defense', 'Leader: +Evasion',
	'Leader: +Mastery', 'Leader: +Max Health', 'Leader: +Max Protection',
	'Leader: +Offense', 'Leader: +Potency',
	'Leader: +Speed', 'Leader: +Tenacity', 'Leader: -Defense',
	'Leader: -Potency', 'Leader: -Speed', 'Leader: Assist',
	'Leader: CD Reduction', 'Leader: Critical Avoid', 'Leader: Protection Up',
	'Leader: TM Gain', 'Leader: TMR']
    fieldContent = ''
    for effect in LEADS:
        fieldContent += '- ' + effect + '\n'
    print(fieldContent)
    print(len(fieldContent))
