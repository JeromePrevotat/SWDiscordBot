###############################################################################
#                         CONSTANTS                                           #
###############################################################################

FEATS = {
    # SECTOR 1
    '1':{
        # Sector Feats
        'Sector':
        '**The Guild :** Defeat 50 enemies with Bounty Hunter\n\t- BH + Bando + Boba\n\n\
        **Unguarded :** Win 5 battles with no Tanks in your Squad\n\t- CLS + Chewpio\n\n\
        **Anticipated Dodge :** Gain Foresight 60 Times\n\t- Jedi : QGJ Lead(optionnal) + GMY + Hoda\n\n\
        **Blinding Assault :** Attempt to inflict Blind 40 times\n\t- CLS + Chewpio\n\n\',
        # Mini Boss Feats
        'Miniboss':
        '**Mini Boss Dash Rendar & Prepared Crew:**\n\
        **Fortunate to be All in One Piece :** Win with URoRRuR\'R\'R surviving\n\t- JML + JKL\n\n\
        **Utinni! :** Win with at least 3 Jawas in your Squad\n\t- JML + JKL\n\n\',
        # Boss Feats
        'Boss':
        '**Boss JKR Jedi:**\n\
        **I\'ll Take Those Odds :** Win witht he Mandalorian surviving\n\t- BH/Maul Mandos/JML\n\n\
        **Amateur Hour :** Win without any Bounty Hunters in your Squad\n\t- Whatever\n\n\',
        },
    # Sector 2
    '2':{
        # Sector Feats
        'Sector':
        '**Flawless Victory :** Win at least 20 battles without losing any units\n\t- Whatever\n\n\
        **Armor Up :** Gain Defense Up 60 times\n\t- Jedi + Old Ben + Zariss + GMY\n\n\
        **All Imperial Troopers :** Win at least 14 battles with a full Squad of Imperial Troopers units\n\t- IT\n\n\
        **Siphoning Strike :** Gain Health Steal Up 20 times\n\t- EP Lead + Vader + Thrawn vs Mini Boss Traya\n\n\',
        # Mini Boss Feats
        'Miniboss':
        '**Mini Boss Traya:**\n\
        **Retreat from Echo Base :** Win with Cpatain Han Solo Surviving\n\t- JML\n\n\
        **End of the Rebellion :** Win without using any Rebels in your Squad\n\t- EP Lead + Vader + Thrawn\n\n\',
        # Boss Feats
        'Boss':
        '**Boss : GG:**\n\
        **Target. Maximum Fire Power :** win with general Veers and SnowTrooper surviving\n\t- IT + IT Tech\n\n\
        **The Empire is Gone :** Win without using any Empire units in your Squad\n\t- Whatever\n\n\',
        },
    # Sector 3
    '3':{
        # Sector Feats
        'Sector':
        '**Lucky Shot :** Score at least 200 Critical Hits\n\t- Whatever\n\n\
        **All Jedi :** Win at least 14 battles with a full Squad of Jedi units\n\t- Jedi : QGJ Lead(optionnal) + GMY + Hoda\n\n\
        **Fleet-Footed :** Evade at least 100 attacks in battles you won\n\t- Jedi : QGJ Lead(optionnal) + GMY + Hoda\n\n\
        **Beep Boop :** Defeat 50 enemies with Droid Units\n\t- GG\n\n\',
        # Mini Boss Feats
        'Miniboss':
        '**Mini Boss MM:**\n\
        **Separatist Leader :** Win with Count dooku and Nute Gunray surviving\n\t- JML JKL Dooku Nute Wat\n\n\
        **For the Republic :** Win without using any Separatists in your Squad\n\t- Whatever\n\n\',
        # Boss Feats
        'Boss':
        '**Boss : DR:**\n\
        **Hello There :** Win with Jedi Knight Anakain and General Kenobi surviving\n\t- JML/JMK/Padme CAT\n\n\
        **All Clone Troopers :** Win with a full Squad of Clone Troopers units\n\t- F that\n\n\',
        },
    # Sector 4
    '4':{
        # Sector Feats
        'Sector':
        '**Forced Tranquility :** Attempt to inflict Ability Block 60 times\n\t- EP Lead Vader Thrawn\n\n\
        **All Sith :** Win 14 battles with a full Squad of Sith units\n\t\- EP Lead Vader Thrawn\n\n\
        **A Clone Army :** Defeat 50 enemies with Clone Tropper units\n\t- Shaak Clones + Zealous Ambition\n\n\
        **Shadowy Dealings :** Gain Stealth 40 times\n\t- Rebels/Resistance + R2\n\n\',
        # Mini Boss Feats
        'Miniboss':
        '**Mini Boss Starkiller :**\n\
        **Battle for Kamino :** Win with clone Sergeant-Phase 1 surviving\n\t- F that\n\n\
        **Crush Them :** Defeat at least 3 enemies in the same time\n\t- F that\n\n\',
        # Boss Feats
        'Boss':
        '**Boss : Lord Vader:**\n\
        **One by One :** Inflict marked on at least 3 enemies\n\t- F that\n\n\
        **Devastating Strike :** Deal at least 200.000 to an enemy in a single hit\n\t- F that\n\n\',
        },
    # Sector 5
    '5':{
        # Sector Feats
        'Sector':
        '**Beskar Breaker :** Inflict Armor Shred 20 times\n\t- JMK/Padme + CAT + GAS\n\n\
        **All Galactic Republic :** Win at least 14 battles with a full Squad of Galactic Republic units\n\t- JMK/Padme + CAT + GAS\n\n\
        **Such a Quiet Thing :** Defeat 50 enemies with Old Republic units\n\t- JML/JKR + Bastilla + Jolee\n\n\
        **Clumsy :** Attempt to inflct Evasion Down 40 times\n\t- CLS + Chewpio\n\n\',
        # Mini Boss Feats
        'Miniboss':
        '**Mini Boss Fat Boba Scoundrels :**\n\
        **This Party\'s Over :** Win with Mace Windu surviving\n\t- JML + JKL + Mace Windu\n\n\
        **Long Live the Empire :** Win with grand Moff tarkin and Moff Gideon surviving\n\t- JML + JKL + Wat + Tarkin + Gideon\n\n\',
        # Boss Feats
        'Boss':
        '**Boss : JMK:**\n\
        **Guarded Assault :** Complete the battle without losing a unit while at least one Attacker is in the Squad\n\t- JMK CAT\n\n\
        **Unsupportive :** Win without using any Support unit in your Squad\n\t- JMK CAT\n\n\',
        },
    # General Feats
    'g':{
        'General':
        '**Live in Light :** Win 50 battles with a full Squad of Light Side units\n\t- Whatever\n\n\
        **Dabble in Darkness :** Win 50 battles with a full Squad of Dark Side units\n\t- GG Sector 3/Sith/IT Sector 2\n\n\
        **Grand Victory :** Defeat at least 500 enemies\n\t- Whatever\n\n\
        **I Want My Armor :** Win 20 battles with Beskar Mando & Boba Fett\n\t- In Sector 1 : BH + Bando + Boba\n\n\
        **Great Shot Kid :** Gain Critical Over 20 Times\n\t- Requires completing A New Hope Feat\n\n\
        **A New Hope :** Win 20 battles with Farmboy Luke and Old Ben\n\t- Rebels/JML + Old Ben + Zariss Sector 2\n\n\
        **Unlimited Power :** Gain Massively Overpowered 20 Times\n\t- Requires completing I Know There is Good in You Feat\n\n\
        **I Know There is Good in You :** Defeat 100 enemies with Darth vader or Jedi Knight Luke Skywalker\n\t- Sith/Empire/Jedi\n\n\
        **Grand Conquest :** Win 250 Battles\n\t- Whatever\n\n\'
        },
}
