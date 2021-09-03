###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os

import swgohgg

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

CWD = os.getcwd()

ABLT_CLASSES = {
	'AAYLASECURA':['Assist', 'Counter', 'Leader: +Tenacity', 'Stun'],
	'ADMIRALACKBAR':['Dispel', 'TM Gain', 'Heal', 'Leader: +Speed',
        'Leader: +Tenacity', 'Assist'],
	'ADMIRALPIETT':['AoE', 'Assist', 'Counter', 'Daze', 'Defense Up',
        'Mass Dispel', 'TM Gain', 'Leader: +Defense', 'Leader: -Speed',
        'Leader: +Potency', 'Offense Up', 'Stealth', 'Fear',
        'Leader: +Offense', 'Leader: -Potency'],
	'AHSOKATANO':['Assist', 'Cleanse', 'TM Gain', 'Heal',
        'Leader: +Evasion', 'Protection Up'],
	'FULCRUMAHSOKA':['Counter', 'Dispel', 'Foresight', 'TM Gain',
        'Buff Steal', 'Protection Up'],
	'AMILYNHOLDO':['AoE', 'Daze', 'Defense Down', 'Dispel', 'Heal',
        'Evasion Down', 'Foresight', 'Taunt'],
	'ARCTROOPER501ST':['Assist', 'Counter', 'True Damage', 'Summon'],
	'ASAJVENTRESS':['AoE', 'Defense Down', 'Mass Dispel', 'TM Gain',
        'Leader: +Speed', 'TMR', 'Stun', 'Leader: +Offense', 'Heal',
		'CD Reduction', 'Stats Stacking'],
	'AURRA_SING':['Counter', 'TM Gain', 'Offense Up', 'CD Reset',
        'Stealth', 'Stun', 'Critical Chance Up', 'Bonus Turn',
        'Leader: TM Gain', 'Leader: +Counter', 'Leader: +Offense'],
	'B1BATTLEDROIDV2':['AoE', 'Assist', 'TM Gain', 'Heal', 'Target Lock'],
	'B2SUPERBATTLEDROID':['AoE', 'Buff Immunity', 'Dispel',
        'Mass Dispel', 'TM Gain', 'CD Reduction',
        'Target Lock', 'Critical Damage Down'],
	'BADBATCHHUNTER':['AoE', 'Bonus Attack', 'Counter', 'Defense Up',
        'Evasion Up', 'Expose', 'TM Gain', 'Leader: +Defense',
        'Leader: +Evasion', 'Leader: +Max Health', 'Offense Up', 'TMR',
        'Stealth', 'Stun', 'Target Lock', 'Critical Chance Up',
        'TM Swap', 'Leader: +Max Protection', 'Leader: +Potency',
        'True Damage'],
	'BADBATCHWRECKER':['AoE', 'Bonus Attack', 'Defense Up', 'Mass Dispel',
        'TM Gain', 'Speed Down', 'Stun', 'Taunt', 'Tenacity Up'],
	'BADBATCHECHO':['AoE', 'Assist', 'Buff Immunity', 'Daze', 'Cleanse',
		'Evasion Up', 'Expose', 'TM Gain', 'Heal Immunity',
		'CD Reduction', 'Defense Up', 'CD Increase', 'Mass Dispel'],
	'BADBATCHOMEGA':['Blind', 'Daze', 'Target Lock', 'TMR', 'Stats Stacking',
	    'Cleanse', 'Stealth', 'Protection Up', 'Defense Penetration Up',
		'TM Gain', 'Protection Over Time', 'Assist'],
	'BADBATCHTECH':['Target Lock', 'Heal', 'Potency Up', 'Stealth',
		'Translation', 'Mass Cleanse', 'Foresight', 'Stealth', 'Tenacity Up',
		'AoE', 'Stun'],
	'BARRISSOFFEE':['Defense Up', 'Cleanse', 'TM Gain', 'Heal',
        'Leader: +Max Health', 'TMR', 'Health Equalization'],
	'BASTILASHAN':['Ability Block', 'Advantage', 'Assist', 'Buff Immunity',
        'Counter', 'Dispel', 'Cleanse', 'TM Gain', 'Leader: +Tenacity',
        'Stun', 'Taunt', 'Leader: Protection Up'],
	'BASTILASHANDARK':['Ability Block', 'Advantage', 'AoE',
        'Evasion Down', 'Expose', 'Foresight', 'TM Gain',
        'Offense Down', 'CD Increase', 'Speed Down', 'Shock', 'Fear',
        'Critical Damage Down', 'Stagger', 'TMR'],
	'BAZEMALBUS':['AoE', 'Assist', 'Counter', 'Mass Dispel', 'TM Gain',
        'Speed Down', 'Taunt', 'Dispel'],
	'BB8':['Advantage', 'Assist', 'Counter', 'Daze', 'Mass Cleanse',
        'Expose', 'Foresight', 'TM Gain', 'Offense Up', 'Speed Up',
        'Taunt', 'Tenacity Down', 'Critical Chance Up', 'Critical Damage Up'],
	'BIGGSDARKLIGHTER':['Assist', 'Evasion Up', 'TM Gain',
        'Critical Chance Up', 'Critical Damage up'],
	'BISTAN':['DoT', 'TM Gain', 'TMR', 'Frenzy'],
	'BOKATAN':['AoE', 'Assist', 'Counter', 'Daze', 'Defense Up',
        'Mass Dispel', 'Leader: +Defense', 'Leader: +Tenacity',
        'Leader: Assist', 'Taunt', 'Tenacity Up', 'Vulnerable'],
	'BOBAFETT':['Ability Block', 'AoE', 'Bonus Attack', 'Counter',
        'Dispel', 'DoT', 'TM Gain', 'Heal Immunity',
        'Leader: +Critical Damage', 'Leader: +Critical Chance',
        'Leader: +Max Health', 'Leader: +Speed',
        'Leader: +Tenacity', 'CD Reduction', 'Revive', 'Taunt',
        'Thermal Detonator', 'Perma Death'],
	'BODHIROOK':['AoE', 'Assist', 'Evasion Down', 'TM Gain', 'Offense Up',
        'Potency Up', 'TMR'],
	'BOSSK':['Assist', 'Dispel', 'Leader: +Defense', 'Leader: +Speed',
        'Leader: +Tenacity', 'Offense Up', 'CD Reduction', 'Stun',
        'Taunt', 'Frenzy', 'Leader: +Max Protection'],
	'C3POLEGENDARY':['Assist', 'Counter', 'Defense Down', 'Expose',
        'TM Gain', 'Offense Down', 'Potency Up', 'CD Reduction',
        'CD Reduction', 'Stealth', 'Confuse', 'Translation', 'TMR',
        'CD Increase', 'Protection Up', 'Passive'],
	'CADBANE':['Advantage', 'AoE', 'Bonus Attack', 'Dispel', 'TM Gain',
        'Leader: +Tenacity', 'CD Reduction', 'TMR', 'Stun',
        'Thermal Detonator', 'Accuracy Down'],
	'CANDEROUSORDO':['AoE', 'Bonus Attack', 'DoT', 'TM Gain',
        'Offense Down', 'Tenacity Down', 'Critical Chance Up',
        'Critical Damage Up'],
	'HOTHHAN':['Daze', 'Cleanse', 'Heal', 'TM Gain', 'Revive'],
	'PHASMA':['Advantage', 'AoE', 'Assist', 'Counter', 'Defense Down',
        'TM Gain', 'Leader: Assist', 'Speed Down'],
	'CARADUNE':['AoE', 'TM Gain', 'Potency Up', 'TMR', 'Revive', 'Stealth',
        'Stun', 'Taunt'],
	'CARTHONASI':['AoE', 'Assist', 'DoT', 'TM Gain', 'Leader: +Tenacity',
        'Leader: Assist', 'Leader: Critical Avoid', 'Offense Up',
        'CD Reset'],
	'CASSIANANDOR':['Ability Block', 'Assist', 'Buff Immunity', 'Counter',
        'Defense Down', 'Defense Up', 'Expose', 'TM Gain',
        'Heal Immunity', 'Offense Down', 'Potency Up', 'Speed Down',
        'Tenacity Up', 'Protection Up'],
	'CC2224':['Assist', 'TM Gain', 'Leader: +Critical Chance',
        'Leader: +Defense', 'Stun', 'CD Reduction'],
	'CHEWBACCALEGENDARY':['AoE', 'Assist', 'Mass Dispel', 'Offense Up',
        'Critical Chance Up', 'CD Reset', 'Stun', 'Tenacity Down'],
	'CHIEFCHIRPA':['Assist', 'Counter', 'TM Gain', 'Heal',
        'Leader: Assist', 'Speed Up'],
	'CHIEFNEBIT':['Assist', 'Leader: +Critical Chance', 'Stealth', 'Taunt',
        'Protection Up', 'CD Reduction', 'Critical Chance Down'],
	'CHIRRUTIMWE':['Assist', 'Counter', 'Mass Cleanse', 'Tenacity Up',
        'Health Equalization', 'Heal'],
	'CHOPPERS3':['AoE', 'Assist', 'Dispel', 'TM Gain', 'Offense Up',
        'CD Reduction', 'Defense Up', 'Speed Up', 'Stun', 'Taunt', 'TMR'],
	'CLONESERGEANTPHASEI':['AoE', 'TM Gain', 'Offense Up', 'TMR'],
	'CLONEWARSCHEWBACCA':['Defense Up', 'Cleanse', 'TM Gain',
        'Leader: +Defense', 'TMR', 'Taunt'],
	'COLONELSTARCK':['AoE', 'Defense Down', 'Dispel', 'TM Gain', 'TMR',
        'Critical Chance Up', 'Critical Damage Up', 'Stagger', 'CD Reduction'],
	'COMMANDERAHSOKA':['Advantage', 'Assist', 'Mass Assist', 'Counter', 'Dispel',
	    'Evasion Up', 'TM Gain', 'TM Swap', 'CD Reduction', 'Insta Kill',
	    'Critical Damage Up', 'Armor Shred', 'Stats Sharing'],
	'COMMANDERLUKESKYWALKER':['Buff Immunity', 'Counter', 'Defense Down',
        'Cleanse', 'TM Gain', 'Leader: +Defense', 'TMR', 'Speed Down',
        'Stun', 'Taunt', 'Tenacity Down', 'Heal', 'Leader: +Offense',
        'Leader: +Counter'],
	'CORUSCANTUNDERWORLDPOLICE':['AoE', 'TM Gain', 'Offense Down', 'Stun'],
	'COUNTDOOKU':['Ability Block', 'Bonus Attack', 'Counter', 'Daze',
        'Cleanse', 'TM Gain', 'Heal Immunity', 'Leader: +Tenacity',
        'Stealth', 'Stun', 'Tenacity Down', 'Shock', 'Leader: +Counter',
        'Critical Hit Immunity'],
	'CT210408':['AoE', 'Assist', 'Mass Dispel', 'Stun', 'Taunt'],
	'CT5555':['Assist', 'Bonus Attack', 'Counter', 'TM Gain',
        'Leader: +Defense', 'Revive', 'Speed Down', 'Taunt'],
	'CT7567':['Counter', 'Mass Cleanse', 'TM Gain', 'Leader: +Max Health',
        'Potency Up', 'CD Reduction', 'TMR', 'Tenacity Up'],
	'DARKTROOPER':['Advantage', 'AoE', 'TM Gain', 'Offense Up', 'Revive'],
	'DARTHMALAK':['Counter', 'Dispel', 'TM Gain', 'Heal Immunity',
        'CD Reset', 'Stun', 'Taunt', 'Tenacity Down', 'Shock',
        'Fear'],
	'MAUL':['Advantage', 'AoE', 'Counter', 'Daze', 'TM Gain',
        'Leader: +Evasion', 'Offense Up', 'Stealth'],
	'DARTHNIHILUS':['AoE', 'Counter', 'Dispel', 'DoT', 'TM Gain',
        'Leader: +Max Health', 'CD Reduction', 'Revive', 'CD Increase',
        'Perma Death', 'Stats Stacking'],
	'DARTHREVAN':['AoE', 'Assist', 'Bonus Attack',
        'Buff Immunity', 'Dispel', 'Foresight', 'TM Gain',
        'Leader: +Critical Chance', 'Leader: +Critical Damage', 'Leader: +Speed',
        'CD Reduction', 'Stun', 'Shock', 'Fear', 'Deathmark'],
	'DARTHSIDIOUS':['AoE', 'Counter', 'DoT', 'Expose', 'TM Gain',
        'Heal Immunity', 'Leader: +Critical Chance'],
	'DARTHSION':['AoE', 'Dispel', 'TM Gain', 'Revive', 'Taunt',
        'Mass Dispel', 'CD Reduction'],
	'DARTHTRAYA':['Ability Block', 'Counter', 'Daze', 'Dispel',
        'Heal Immunity', 'Leader: +Max Health', 'CD Reduction',
        'Tenacity Down', 'Dispel', 'CD Increase', 'Protection Up',
        'Leader: +Critical Avoid', 'Leader: +Potency', 'Cleanse'],
	'VADER':['Ability Block', 'AoE', 'DoT', 'TM Gain', 'Speed Down',
        'Bonus Turn', 'Leader: +Offense', 'Leader: TMR'],
	'DATHCHA':['Ability Block', 'AoE', 'Defense Down',
        'TMR', 'Stealth', 'Stun'],
	'DEATHTROOPER':['AoE', 'Bonus Attack', 'Daze', 'Dispel', 'TM Gain',
        'Heal Immunity', 'Stun', 'CD Increase', 'Deathmark',
        'Perma Death'],
	'DENGAR':['AoE', 'Assist', 'DoT', 'TM Gain', 'Speed Down',
        'Stealth', 'Stun', 'Tenacity Down', 'Tenacity Up', 'TMR',
        'Thermal Detonator'],
	'DIRECTORKRENNIC':['Ability Block', 'AoE', 'Assist', 'Buff Immunity',
        'Leader: +Critical Chance', 'Revive', 'Speed Down', 'Stun',
        'Tenacity Down', 'Stagger', 'Leader: +Potency'],
	'DROIDEKA':['Assist', 'Dispel', 'TM Gain', 'Target Lock',
        'Tenacity Up', 'True Damage', 'Damage Immunity'],
	'EETHKOTH':['Ability Block', 'Defense Down',
        'Leader: +Defense', 'Stun'],
	'EMBO':['Counter', 'Dispel', 'Foresight', 'Offense Up',
        'Leader: +Counter'],
	'EMPERORPALPATINE':['AoE', 'Counter', 'Dispel', 'TM Gain',
        'Leader: +Evasion', 'Leader: +Max Health', 'Offense Up', 'Stun',
        'Shock', 'Leader: +Potency', 'Stats Stacking'],
	'ENFYSNEST':['AoE', 'Buff Immunity', 'Counter', 'Daze', 'Dispel',
        'Expose', 'TM Gain', 'TMR', 'Stun', 'Stats Stacking'],
	'EWOKELDER':['Assist', 'Mass Cleanse', 'TM Gain', 'Heal', 'Revive',
        'CD Reduction'],
	'EWOKSCOUT':['Assist', 'TM Gain'],
	'EZRABRIDGERS3':['Assist', 'Bonus Attack', 'Defense Up', 'Dispel',
        'TM Gain', 'CD Reduction'],
	'FINN':['Advantage', 'Counter', 'Defense Up', 'Mass Cleanse', 'Expose',
        'TM Gain', 'Leader: +Defense', 'Stun', 'Taunt', 'Heal',
        'Leader: +Offense', 'Leader: +Potency', 'Leader: TMR',
        'Leader: CD Reduction'],
	'FIRSTORDEREXECUTIONER':['Advantage', 'Dispel', 'TM Gain',
        'TMR', 'CD Reset', 'Stats Stacking'],
	'FIRSTORDEROFFICERMALE':['Advantage', 'Cleanse', 'TM Gain',
        'Offense Up', 'TMR', 'Tenacity Up', 'CD Reduction'],
	'FIRSTORDERSPECIALFORCESPILOT':['Advantage', 'AoE', 'Assist',
        'Defense Down', 'Speed Up', 'Stun'],
	'FIRSTORDERTROOPER':['Advantage', 'Assist', 'Counter', 'Defense Up',
        'Cleanse', 'TM Gain', 'Speed Down', 'Taunt'],
	'FIRSTORDERTIEPILOT':['Advantage', 'Bonus Attack', 'Buff Immunity',
        'Foresight', 'Offense Down', 'Health Down'],
	'GAMORREANGUARD':['Counter', 'DoT', 'Expose', 'Taunt'],
	'GARSAXON':['AoE', 'Assist', 'Counter', 'Leader: +Defense',
        'CD Reduction', 'Speed Down', 'TMR', 'Leader: +Counter'],
	'ZEBS3':['Counter', 'Daze', 'Expose', 'TM Gain', 'Stun',
        'Tenacity Up', 'Stagger', 'Protection Up'],
	'GRIEVOUS':['AoE', 'Counter', 'Cleanse', 'TM Gain', 'Heal Immunity',
        'Leader: -Defense', 'TMR', 'CD Reset', 'Stun',
        'Target Lock', 'Bonus Turn'],
	'GENERALHUX':['Advantage', 'AoE', 'Assist', 'Counter', 'Mass Dispel',
        'TM Gain', 'CD Reset', 'Cleanse', 'Bonus Turn'],
	'GENERALKENOBI':['Advantage', 'Assist', 'Counter', 'Mass Cleanse',
        'Foresight', 'TM Gain', 'Leader: +Defense', 'Leader: +Max Health',
        'Leader: Assist', 'Offense Up', 'Stealth', 'Taunt',
        'Critical Hit Immunity'],
	'GENERALSKYWALKER':['AoE', 'Counter', 'Daze', 'Cleanse', 'TM Gain',
        'Leader: +Speed', 'CD Reduction', 'TMR', 'CD Reset',
        'Revive', 'Taunt', 'CD Increase', 'Armor Shred', 'Perma Death',
        'Leader: +Critical Damage', 'Stats Stacking', 'Critical Hit Immunity'],
	'VEERS':['Ability Block', 'AoE', 'Assist', 'TM Gain', 'Leader: +Speed',
        'Offense Up', 'Speed Up', 'Leader: +Offense'],
	'GEONOSIANBROODALPHA':['AoE', 'Assist', 'Counter', 'Dispel', 'Expose',
        'TM Gain', 'Leader: +Max Health', 'Offense Up', 'TMR', 'Revive',
        'Taunt', 'Mass Dispel', 'Summon', 'Critical Damage Up', 'Heal',
        'CD Reduction', 'Health Equalization', 'Leader: +Max Protection'],
	'GEONOSIANSOLDIER':['Assist', 'TM Gain', 'Tenacity Down'],
	'GEONOSIANSPY':['AoE', 'Counter', 'Dispel', 'Evasion Down', 'Expose',
        'TM Gain', 'Potency Up', 'Stealth', 'Critical Chance Up', 'Cleanse',
        'CD Reduction'],
	'GRANDADMIRALTHRAWN':['Ability Block', 'Counter', 'Defense Down',
        'Dispel', 'TM Gain', 'TMR', 'Speed Down', 'Speed Up', 'Stun',
        'Cleanse', 'Leader: +Max Protection', 'Leader: +Offense',
        'TM Swap'],
	'GRANDMASTERYODA':['AoE', 'Foresight', 'TM Gain',
        'Leader: +Critical Chance',
        'Leader: +Tenacity', 'Offense Up', 'TMR', 'Stealth', 'Stun',
        'Taunt', 'Tenacity Up', 'Potency Down', 'Buff Steal', 'Bonus Turn',
        'Protection Up', 'Leader: +Critical Chance', 'Leader: +Critical Damage'],
	'GRANDMOFFTARKIN':['AoE', 'Defense Down', 'Expose', 'TM Gain',
        'Leader: +Speed', 'Offense Down', 'Potency Up',
        'TMR', 'Stats Stacking', 'Critical Chance Down'],
	'GREEDO':['AoE', 'Bonus Attack', 'Counter', 'Dispel', 'TM Gain',
        'Potency Up', 'TMR', 'Stun', 'Thermal Detonator', 'Critical Chance Up',
        'Leader: +Critical Damage'],
	'GREEFKARGA':['Assist', 'Counter', 'Daze', 'Dispel', 'TM Gain',
        'Leader: +Critical Chance', 'Offense Up', 'Stealth', 'Tenacity Up',
        'Critical Damage Up', 'Critical Chance Up', 'Mass Cleanse', 'Heal',
        'CD Reduction', 'Leader: +Max Protection', 'Leader: +Offense'],
	'HANSOLO':['Counter', 'Evasion Up', 'TM Gain', 'TMR', 'Stun', 'Taunt',
    'Critical Chance Up', 'Critical Damage Up', 'Bonus Attack', 'Bonus Turn'],
	'HERASYNDULLAS3':['Assist', 'Cleanse', 'Expose', 'TM Gain',
        'CD Reduction', 'Revive'],
	'HERMITYODA':['Assist', 'Counter', 'Cleanse', 'Foresight', 'TM Gain',
        'Heal', 'Heal Immunity', 'CD Reset', 'Stealth',
        'Health Equalization', 'Passive'],
	'HK47':['AoE', 'Counter', 'Dispel', 'TM Gain', 'Leader: +Critical Chance',
        'Offense Up', 'CD Reset', 'Tenacity Down', 'True Damage',
        'CD Reduction', 'Leader: +Critical Damage'],
	'HOTHREBELSCOUT':['TM Gain', 'Stun'],
	'HOTHREBELSOLDIER':['Counter', 'Defense Up', 'Offense Down', 'Taunt',
        'Health Up'],
	'MAGNAGUARD':['AoE', 'Counter', 'Dispel', 'CD Reset', 'Speed Up',
        'Stealth', 'Stun', 'Target Lock', 'Taunt', 'Cleanse',
        'Mass Cleanse', 'Bonus Turn'],
	'IG11':['AoE', 'Assist', 'Counter', 'Cleanse', 'DoT', 'Foresight',
        'Taunt', 'Tenacity Down', 'Heal'],
	'IG86SENTINELDROID':['Assist'],
	'IG88':['Ability Block', 'AoE', 'Defense Down', 'DoT', 'Heal Immunity',
        'Leader: +Critical Chance', 'Target Lock'],
	'IMAGUNDI':['Counter', 'Defense Down', 'Leader: +Defense',
        'Defense Up', 'Leader: +Counter'],
	'IMPERIALPROBEDROID':['AoE', 'Mass Dispel', 'Expose', 'TM Gain', 'TMR',
        'Target Lock', 'Perma Death'],
	'IMPERIALSUPERCOMMANDO':['Bonus Attack', 'Buff Immunity', 'Counter',
        'Dispel', 'TM Gain', 'Offense Down'],
	'JANGOFETT':['AoE', 'Counter', 'Dispel', 'TM Gain', 'Heal Immunity',
        'Leader: +Critical Chance', 'Leader: +Speed', 'Leader: +Tenacity',
        'Revive', 'Taunt', 'Bonus Attack', 'Stagger', 'Burning',
        'Perma Death', 'Damage Immunity'],
	'JAWA':['AoE', 'TM Gain', 'Speed Down', 'Stun'],
	'JAWAENGINEER':['TM Gain', 'Heal', 'Revive', 'Thermal Detonator',
        'Critical Chance Up'],
	'JAWASCAVENGER':['AoE', 'Defense Down', 'Heal Immunity',
        'Offense Down', 'Offense Up', 'Stealth', 'Tenacity Down',
        'Thermal Detonator'],
	'JEDIKNIGHTCONSULAR':['Heal', 'CD Reduction', 'TM Gain'],
	'ANAKINKNIGHT':['Advantage', 'AoE', 'Buff Immunity', 'Dispel',
        'Heal Immunity', 'Offense Up', 'Critical Chance Up', 'Protection Up',
        'Mass Dispel', 'Leader: +Offense', 'Leader: +Critical Damage',
        'Bonus Turn'],
	'JEDIKNIGHTGUARDIAN':['Ability Block', 'AoE', 'Defense Up',
        'Offense Down'],
	'JEDIKNIGHTLUKE':['AoE', 'Assist', 'Counter', 'Dispel', 'TM Gain',
        'Leader: +Critical Chance', 'Leader: +Speed', 'Leader: Assist', 'Stun',
        'Vulnerable', 'Blind', 'Leader: +Critical Damage'],
	'JEDIKNIGHTREVAN':['Ability Block', 'Advantage', 'AoE', 'Assist',
        'Buff Immunity', 'Counter', 'Dispel', 'Foresight', 'TM Gain',
        'Leader: +Max Health', 'Leader: +Speed', 'Leader: +Tenacity',
        'Leader: Assist', 'CD Reduction', 'Stun', 'Taunt', 'Tenacity Up',
        'Mass Cleanse', 'Heal', 'Critical Damage Up', 'TM Swap', 'Marked',
        'CD Increase', 'TMR', 'Leader: +Critical Chance', 'Cleanse',
        'Critical Hit Immunity', 'Bonus Turn'],
	'JEDIMASTERKENOBI':['Mass Cleanse', 'Protection Up', 'Heal', 'Counter',
	    'Ability Block', 'Defense Penetration Up', 'Vulnerable',
	    'Heal Immunity', 'Assist', 'Foresight', 'Tenacity Up', 'Damage Immunity',
	    'CD Reset', 'Leader: +Mastery', 'Leader: +Max Health', 'Leader: +Speed',
	    'Leader: Protection Up', 'Stats Stacking'],
	'GRANDMASTERLUKE':['Ability Block', 'Advantage', 'AoE', 'Assist',
        'Buff Immunity', 'Counter', 'Daze', 'Defense Up',
        'Expose', 'TM Gain', 'Leader: +Max Health',
        'Leader: +Speed', 'Leader: Assist',
        'CD Reduction', 'TMR', 'CD Reset', 'Stun', 'Taunt',
        'Tenacity Down', 'Tenacity Up', 'Mass Cleanse', 'Critical Chance Up',
        'Critical Damage Up', 'CD Increase', 'Breach', 'Critical Hit Immunity',
        'Leader: +Max Protection', 'Leader: +Offense', 'Cleanse',
        'Defense Up', 'True Damage'],
	'JOLEEBINDO':['Assist', 'Dispel', 'TM Gain', 'Revive', 'CD Reduction',
        'Heal', 'Cleanse', 'Critical Hit Immunity', 'Protection Up'],
	'JUHANI':['AoE', 'Counter', 'Mass Cleanse', 'Offense Up', 'Stealth',
        'Stun', 'Taunt', 'Stagger'],
	'JYNERSO':['Advantage', 'AoE', 'Expose', 'TM Gain', 'TMR', 'Revive',
        'Stun', 'Leader: +Potency'],
	'K2SO':['Assist', 'Counter', 'Daze', 'Dispel', 'Offense Down',
        'Taunt'],
	'KANANJARRUSS3':['Counter', 'Defense Up', 'Cleanse', 'Foresight',
        'TM Gain', 'Offense Down', 'Taunt', 'Mass Cleanse',
        'Protection Up'],
	'KIADIMUNDI':['AoE', 'Bonus Attack', 'Counter', 'Daze', 'Cleanse',
        'TM Gain', 'CD Reset', 'Taunt', 'Mass Cleanse',
        'Armor Shred'],
	'KITFISTO':['AoE', 'Bonus Attack', 'Counter', 'TM Gain',
        'Leader: +Defense', 'Leader: +Tenacity', 'Potency Up'],
	'KUIIL':['Expose', 'TM Gain', 'Heal', 'Revive', 'Speed Down', 'Stun',
        'Burning', 'Shock'],
	'KYLOREN':['AoE', 'Counter', 'DoT', 'TM Gain',
        'Heal Immunity', 'CD Reset', 'Stun'],
	'KYLORENUNMASKED':['Advantage', 'Counter', 'Dispel', 'TM Gain',
        'Leader: +Speed', 'Stun', 'Taunt', 'Tenacity Down',
        'Leader: +Critical Damage', 'Pre Taunt'],
	'L3_37':['Counter', 'Defense Down', 'Cleanse', 'TM Gain', 'Taunt',
        'Tenacity Up', 'Stats Stacking', 'Heal', 'Health Equalization',
        'CD Reduction', 'Pre Taunt'],
	'ADMINISTRATORLANDO':['AoE', 'Leader: +Speed', 'CD Reset',
        'Leader: +Critical Damage', 'Critical Chance Up'],
	'LOBOT':['Defense Down', 'Mass Cleanse', 'TM Gain', 'Heal',
        'Leader: +Speed', 'Leader: +Potency'],
	'LOGRAY':['Advantage', 'AoE', 'Assist', 'Daze', 'Dispel', 'Foresight',
        'TM Gain', 'Offense Up', 'TMR', 'Tenacity Up', 'Health Up'],
	'LUKESKYWALKER':['Advantage', 'Counter', 'Defense Down', 'Dispel',
        'DoT', 'TM Gain', 'Leader: +Tenacity', 'Speed Down', 'Stun',
        'Stats Stacking'],
	'LUMINARAUNDULI':['Ability Block', 'Evasion Up', 'Heal',
        'Leader: +Evasion'],
	'MACEWINDU':['Dispel', 'Expose', 'TM Gain', 'Leader: +Critical Chance',
        'Leader: +Offense'],
	'MAGMATROOPER':['AoE', 'TM Gain', 'TMR'],
	'MAULS7':['Dispel', 'Offense Down', 'True Damage', 'Buff Immunity',
	    'CD Increase', 'Bonus Turn', 'Leader: +Max Health', 'Leader: +Offense',
	    'Frenzy', 'Retribution', 'Counter'],
	'MISSIONVAO':['Assist', 'Daze', 'Cleanse', 'DoT', 'TM Gain',
        'Stealth', 'Protection Up', 'Blind'],
	'HUMANTHUG':['Defense Down', 'TM Gain', 'Offense Up',
        'Thermal Detonator'],
	'MOFFGIDEONS1':['AoE', 'Assist', 'Counter', 'Daze', 'Dispel',
        'TM Gain', 'Leader: +Max Health', 'Revive', 'TMR', 'Protection Up',
        'Armor Shred', 'Leader: +Max Protection', 'Stats Stacking'],
	'MONMOTHMA':['Assist', 'Cleanse', 'Leader: Assist',
        'Revive', 'Taunt', 'Health Equalization', 'Summon',
        'CD Reduction', 'Stats Sharing', 'Untargetable', 'Passive'],
	'MOTHERTALZIN':['AoE', 'Assist', 'Counter', 'TM Gain',
        'Leader: +Speed', 'Leader: Assist', 'Revive', 'Leader: +Potency'],
	'NIGHTSISTERACOLYTE':['Cleanse', 'TM Gain', 'Stealth',
        'CD Reduction'],
	'NIGHTSISTERINITIATE':['Buff Immunity', 'Counter', 'DoT',
        'Critical Chance Up'],
	'NIGHTSISTERSPIRIT':['Dispel', 'Foresight', 'TM Gain',
        'TMR', 'Speed Down', 'Stun'],
	'NIGHTSISTERZOMBIE':['Counter', 'Cleanse', 'Revive', 'Taunt',
        'Tenacity Down', 'Heal'],
	'NUTEGUNRAY':['AoE', 'Assist', 'Dispel', 'Leader: +Speed',
        'CD Reduction', 'Revive', 'Speed Down', 'Stealth', 'CD Increase',
        'Leader: +Potency'],
	'OLDBENKENOBI':['Ability Block', 'AoE', 'Defense Up', 'Evasion Down',
        'TM Gain', 'Leader: +Evasion', 'Offense Down', 'Offense Up',
        'Potency Up', 'TMR', 'Speed Up', 'Taunt'],
	'DAKA':['Defense Up', 'TM Gain', 'Heal', 'Leader: +Defense',
        'Offense Up', 'Revive', 'Stun', 'Leader: +Max Health',
        'CD Reduction', 'Stats Stacking'],
	'PADMEAMIDALA':['Assist', 'Dispel', 'TM Gain', 'Leader: +Max Health',
        'Stun', 'Protection Up', 'Heal', 'Mass Cleanse', ],
	'PAO':['AoE', 'Defense Down', 'TM Gain', 'Offense Up', 'CD Reduction'],
	'PAPLOO':['Assist', 'Defense Up', 'Dispel', 'TM Gain', 'Speed Down',
        'Taunt', 'Cleanse'],
	'PLOKOON':['AoE', 'Defense Up', 'Dispel', 'TM Gain', 'Offense Down',
        'Offense Up'],
	'POE':['Buff Immunity', 'Expose', 'Offense Down', 'TMR', 'Taunt',
        'Leader: +Offense', 'Leader: +Potency'],
	'POGGLETHELESSER':['Ability Block', 'Assist', 'Mass Cleanse',
        'TM Gain', 'Offense Up', 'TMR', 'Leader: +Offense'],
	'PRINCESSLEIA':['Bonus Attack', 'Foresight', 'TM Gain',
        'Leader: +Critical Chance', 'Offense Up', 'Stealth', 'Critical Damage Up',
        'Critical Chance up'],
	'QIRA':['AoE', 'Assist', 'Counter', 'Daze', 'Dispel', 'Expose',
        'TM Gain', 'Leader: +Critical Chance', 'Leader: +Speed', 'Offense Down',
        'Mass Dispel', 'Stagger', 'Leader: +Offense'],
	'QUIGONJINN':['Assist', 'Counter', 'Dispel', 'Foresight', 'TM Gain',
        'Leader: +Speed', 'Foresight' 'Offense Up', 'TMR'],
	'R2D2_LEGENDARY':['Advantage', 'AoE', 'Cleanse', 'Foresight',
        'TM Gain', 'Revive', 'Stealth', 'Stun', 'Burning',
        'Stats Sharing'],
	'RANGETROOPER':['Assist', 'Counter', 'Protection Up'],
	'HOTHLEIA':['Ability Block', 'Buff Immunity', 'Counter', 'Foresight',
        'TM Gain', 'Leader: +Critical Chance', 'Leader: +Tenacity',
        'CD Reduction'],
	'EPIXFINN':['AoE', 'Assist', 'Counter', 'Mass Cleanse', 'TM Gain', 'Taunt',
        'CD Reduction', 'TM Swap'],
	'EPIXPOE':['Buff Immunity', 'Daze', 'Dispel', 'DoT', 'Stun',
        'Vulnerable', 'Stagger'],
	'RESISTANCEPILOT':['Expose', 'Foresight', 'TM Gain'],
	'RESISTANCETROOPER':['Dispel', 'Expose', 'TM Gain', 'Speed Down',
        'CD Reduction'],
	'GLREY':['AoE', 'Counter', 'Cleanse', 'Leader: +Max Health',
        'Leader: +Speed', 'Perma Death', 'Stun', 'True Damage',
        'Critical Hit Immunity', 'Leader: +Mastery', 'Damage Immunity'],
	'REYJEDITRAINING':['Ability Block', 'Assist', 'Counter', 'Daze',
        'Dispel', 'Expose', 'Foresight', 'TM Gain', 'Heal Immunity',
        'Leader: +Critical Chance', 'Offense Down', 'Offense Up',
        'CD Reduction', 'TMR', 'Speed Down', 'Cleanse',
        'Leader: +Critical Damage', 'Critical Damage Up'],
	'REY':['Daze', 'Foresight', 'Offense Up'],
	'ROSETICO':['Bonus Attack', 'Daze', 'Defense Up', 'Expose', 'TM Gain',
        'TMR', 'Stun', 'Tenacity Up'],
	'ROYALGUARD':['Defense Up', 'TM Gain', 'Speed Down', 'Stun', 'Taunt',
        'Health Up'],
	'SABINEWRENS3':['AoE', 'Counter', 'Expose', 'Offense Up',
        'CD Reduction', 'Armor Shred', 'Stagger', 'Critical Chance Up'],
	'SAVAGEOPRESS':['Defense Up', 'Cleanse', 'TM Gain', 'Leader: +Defense',
        'Leader: +Tenacity', 'Offense Down', 'Offense Up',
        'Critical Chance Up', 'Critical Damage Up'],
	'SCARIFREBEL':['AoE', 'TM Gain', 'Offense Down', 'Offense Up',
        'Revive', 'Speed Up', 'Taunt', 'Accuracy Up'],
	'SHAAKTI':['Assist', 'Counter', 'Dispel', 'TM Gain',
        'Leader: +Max Health', 'Leader: +Speed', 'Offense Up', 'Speed Up',
        'Stealth', 'Taunt', 'Tenacity Up', 'Mass Cleanse',
        'Critical Chance Up', 'Critical Hit Immunity', 'Leader: +Max Protection',
        'Leader: +Offense'],
	'SHORETROOPER':['Counter', 'TM Gain', 'Heal', 'Taunt',
        'Critical Chance Down', 'Critical Hit Immunity', 'CD Reduction', 'Pre Taunt'],
	'SITHASSASSIN':['Cleanse', 'Evasion Down', 'Foresight', 'TM Gain',
        'Offense Up', 'Speed Up', 'Stealth', 'Stun', 'Tenacity Up'],
	'SITHTROOPER':['AoE', 'Counter', 'Defense Down', 'Defense Up',
        'Offense Down', 'Taunt', 'Protection Up'],
	'SITHPALPATINE':['Ability Block', 'AoE', 'Assist', 'Counter',
        'Mass Cleanse', 'Expose', 'TM Gain', 'Leader: +Defense',
        'Leader: +Speed', 'Revive', 'Speed Up', 'Stun', 'Leader: +Mastery',
        'Shock', 'CD Reduction', 'Mass Dispel', 'Perma Death',
        'Untargetable', 'Leader: +Potency', 'Insta Kill'],
	'SITHMARAUDER':['TM Gain', 'Offense Down', 'Potency Up'],
	'FOSITHTROOPER':['Advantage', 'AoE', 'Assist', 'Mass Cleanse',
        'CD Reset', 'Stun', 'Critical Hit Immunity', 'Bonus Turn'],
	'SNOWTROOPER':['Ability Block', 'AoE', 'TM Gain', 'Critical Damage Up',
        'CD Reduction'],
	'STORMTROOPER':['Expose', 'TMR', 'Taunt', 'Defense Up',
        'Protection Up'],
	'STORMTROOPERHAN':['TM Gain', 'Leader: +Defense', 'TMR', 'Taunt',
        'Leader: +Offense'],
	'SUNFAC':['Counter', 'Daze', 'Defense Up', 'Dispel', 'Offense Down',
        'TMR', 'Taunt', 'Stagger', 'Blind', 'Critical Chance Down',
        'Health Up'],
	'SUPREMELEADERKYLOREN':['Advantage', 'AoE', 'Buff Immunity', 'Counter',
        'Cleanse', 'TM Gain', 'Leader: +Mastery', 'Leader: +Speed',
        'Revive', 'Stun', 'Damage Immunity', 'CD Reset',
        'Mass Dispel', 'Mass Cleanse', 'Leader: +Critical Damage',
        'Critical Damage Up', 'Perma Death', 'Stats Stacking'],
	'T3_M4':['Ability Block', 'AoE', 'Cleanse', 'Offense Down',
        'Offense Up', 'TMR', 'Target Lock', 'Heal', 'Critical Hit Immunity',
        'Mass Dispel', 'Critical Chance Down'],
	'TALIA':['Mass Cleanse', 'DoT', 'TM Gain', 'Leader: +Evasion',
        'Heal', 'Stagger'],
	'BADBATCHTECH':['AoE', 'Bonus Attack', 'Daze', 'Mass Cleanse',
        'Foresight', 'Potency Up', 'CD Reduction', 'CD Reset',
        'Stealth', 'Stun', 'Target Lock', 'Tenacity Up', 'Heal',
        'Translation'],
	'TEEBO':['Dispel', 'TM Gain', 'TMR', 'Stealth'],
	'ARMORER':['Assist', 'Counter', 'Dispel', 'Armor Shred',
        'Protection Up', 'Critical Hit Immunity'],
	'THEMANDALORIAN':['Assist', 'TM Gain',
        'Leader: +Critical Chance', 'Leader: +Speed', 'Leader: +Tenacity',
        'Revive', 'Critical Chance Up', 'Critical Damage Up', 'CD Reduction',
        'Insta Kill', 'Perma Death'],
	'THEMANDALORIANBESKARARMOR':['Ability Block', 'AoE', 'Assist',
        'Counter', 'Mass Cleanse', 'DoT', 'TM Gain', 'Leader: +Max Health',
        'TMR', 'CD Reset', 'Stealth', 'Taunt', 'Tenacity Up',
        'Bonus Attack', 'True Damage', 'Damage Immunity',
        'Leader: +Max Protection', 'Leader: +Offense', 'Cleanse'
        'Bonus Turn'],
	'C3POCHEWBACCA':['Advantage', 'AoE', 'Assist', 'Counter',
        'Mass Dispel', 'Evasion Down', 'Revive', 'Cleanse', 'Blind',
        'Stats Stacking', 'Stats Sharing'],
	'TIEFIGHTERPILOT':['Ability Block', 'AoE', 'Buff Immunity',
        'Foresight', 'Tenacity Down'],
	'TUSKENRAIDER':['Assist', 'TMR'],
	'TUSKENSHAMAN':['DoT', 'TM Gain', 'Offense Up', 'Heal'],
	'UGNAUGHT':['AoE', 'Defense Down', 'TM Gain', 'Stun'],
	'URORRURRR':['TM Gain', 'Leader: +Defense', 'Offense Up', 'Speed Up',
        'Stun'],
	'YOUNGCHEWBACCA':['Advantage', 'AoE', 'Counter', 'Revive',
        'Protection Up', 'CD Reduction', ],
	'SMUGGLERCHEWBACCA':['AoE', 'Daze', 'Dispel', 'TM Gain', 'CD Reset',
        'Speed Down', 'Stun', 'Bonus Turn'],
	'SMUGGLERHAN':['Ability Block', 'AoE', 'Bonus Attack', 'Counter',
        'TM Gain', 'CD Reset', 'Stun', 'Bonus Turn'],
	'VISASMARR':['AoE', 'Assist', 'Counter', 'Cleanse', 'Revive',
        'CD Reduction', 'Heal'],
	'WAMPA':['AoE', 'Counter', 'Daze', 'Cleanse', 'Protection Up', 'DoT',
        'TM Gain', 'Heal Immunity', 'Stun'],
	'WATTAMBOR':['Assist', 'Cleanse', 'DoT', 'TM Gain', 'TMR', 'Revive',
        'Passive', 'Bonus Turn'],
	'WEDGEANTILLES':['AoE', 'Defense Down', 'Leader: +Offense', 'TM Gain'],
	'WICKET':['AoE', 'Assist', 'TM Gain', 'Stealth', 'Critical Chance Up',
        'Critical Damage Up', 'Bonus Turn'],
	'YOUNGHAN':['Assist', 'Counter', 'Speed Down', 'Protection Up',
        'Critical Damage Up', 'Stats Stacking'],
	'YOUNGLANDO':['Ability Block', 'Counter', 'Cleanse', 'Potency Up',
        'TM Gain', 'Potency Down', 'Speed Up', 'Stealth', 'CD Reduction'],
	'ZAALBAR':['AoE', 'Counter', 'DoT', 'Taunt', 'Armor Shred'],
	'ZAMWESELL':['AoE', 'Counter', 'Cleanse', 'Evasion Down',
        'Leader: +Potency', 'TM Gain', 'Speed Up', 'Stealth',
        'Thermal Detonator'],
}

BUFFS = ['Accuracy Up', 'Advantage', 'Critical Chance Up',
	'Critical Damage Up', 'Critical Hit Immunity', 'Damage Immunity',
	'Defense Up', 'Evasion Up', 'Foresight', 'Frenzy', 'Health Up',
	'Offense Up', 'Potency Up', 'Protection Up', 'Speed Up', 'Stealth',
	'Taunt', 'Tenacity Up', 'Translation', 'Retribution', 'Protection Over Time']
DEBUFFS = ['Ability Block', 'Accuracy Down', 'Armor Shred', 'Blind', 'Breach',
	'Buff Immunity', 'Burning', 'Confuse', 'Critical Chance Down',
	'Critical Damage Down', 'Daze', 'Deathmark', 'Defense Down', 'DoT',
	'Evasion Down', 'Expose', 'Fear', 'Heal Immunity', 'Health Down', 'Marked',
	'Offense Down', 'Potency Down', 'Shock', 'Speed Down', 'Stun',
	'Target Lock', 'Tenacity Down', 'Thermal Detonator', 'Vulnerable']
MISCS = ['AoE', 'Assist', 'Bonus Attack', 'Bonus Turn', 'Buff Steal',
	'CD Increase', 'CD Reduction', 'CD Reset', 'Cleanse', 'Counter', 'Dispel',
	'Heal', 'Health Equalization', 'Insta Kill', 'Mass Cleanse', 'Mass Dispel',
	'Passive', 'Perma Death', 'Pre Taunt', 'Revive', 'Stagger',
	'Stats Sharing', 'Stats Stacking', 'Summon', 'TM Gain', 'TM Swap', 'TMR',
	'True Damage', 'Untargetable']
LEADS = ['Leader: +Counter', 'Leader: +Critical Avoid',
	'Leader: +Critical Chance', 'Leader: +Critical Damage',
	'Leader: +Defense', 'Leader: +Evasion',
	'Leader: +Mastery', 'Leader: +Max Health', 'Leader: +Max Protection',
	'Leader: +Offense', 'Leader: +Potency',
	'Leader: +Speed', 'Leader: +Tenacity', 'Leader: -Defense',
	'Leader: -Potency', 'Leader: -Speed', 'Leader: Assist',
	'Leader: CD Reduction', 'Leader: Critical Avoid', 'Leader: Protection Up',
	'Leader: TM Gain', 'Leader: TMR']

ABLT_CLASSES_LIST = {
	'Buffs':BUFFS,
	'Debuffs':DEBUFFS,
	'Miscs':MISCS,
	'Leads':LEADS,
	}

if __name__ == '__main__':
	client = swgohgg.Swgohgg()
	charList = client.get_from_api('characters')
	tags = []
	with open(CWD + os.sep + 'trash', 'w+') as f:
		for character in charList:
			if (character['name'] == 'Tech'
				or character['name'] == 'Hunter'):
					f.write('\'{}\':{}\n'.format(character['base_id'],
						character['ability_classes']))
