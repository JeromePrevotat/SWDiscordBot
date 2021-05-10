EN_US = 'EN-US'
FR_FR = 'FR-FR'

LOCALIZATIONS = [
    {
        'local':'EN-US',
        # LOCALS
        'EN-US':'English',
        'FR-FR':'Français',
        # COMMANDS
        # Missing arguments
        'missing_arg':'Missing arguments. Check %help for more informations.',
        # Local
        'local_success':'Bot new local set to ',
        'local_fail':'Could not find local ',
        # Have
        'have_success':'Characters with ',
        'have_fail':'No Character seems to interact with ',
        # Ability Classes
        'Ability Block':'Ability Block',
        'Accuracy Down':'Accuracy Down',
        'Accuracy Up':'Accuracy Up',
        'Advantage':'Advantage',
        'AoE':'AoE',
        'Armor Shred':'Armor Shred',
        'Assist':'Assist',
        'Blind':'Blind',
        'Bonus Attack':'Bonus Attack',
        'Bonus Turn':'Bonus Turn',
        'Breach':'Breach',
        'Buff Immunity':'Buff Immunity',
        'Buff Steal':'Buff Steal',
        'Burning':'Burning',
        'CD Increase':'CD Increase',
        'CD Reduction':'CD Reduction',
        'CD Reset':'CD Reset',
        'Cleanse':'Cleanse',
        'Confuse':'Confuse',
        'Counter':'Counter',
        'Crit Chance Down':'Crit Chance Down',
        'Crit Chance Up':'Crit Chance Up',
        'Crit Damage Down':'Crit Damage Down',
        'Crit Damage Up':'Crit Damage Up',
        'Crit Immunity':'Crit Immunity',
        'Damage Immunity':'Damage Immunity',
        'Daze':'Daze',
        'Deathmark':'Deathmark',
        'Defense Down':'Defense Down',
        'Defense Up':'Defense Up',
        'Dispel':'Dispel',
        'DoT':'DoT',
        'Evasion Down':'Evasion Down',
        'Evasion Up':'Evasion Up',
        'Expose':'Expose',
        'Fear':'Fear',
        'Foresight':'Foresight',
        'Frenzy':'Frenzy',
        'Heal':'Heal',
        'Heal Immunity':'Heal Immunity',
        'Health Down':'Health Down',
        'Health Equalization':'Health Equalization',
        'Health Up':'Health Up',
        'Insta Kill':'Insta Kill',
        'Leader: +Counter':'Leader: +Counter',
        'Leader: +Crit Avoid':'Leader: +Crit Avoid',
        'Leader: +Crit Chance':'Leader: +Crit Chance',
        'Leader: +Crit Damage':'Leader: +Crit Damage',
        'Leader: +Defense':'Leader: +Defense',
        'Leader: +Evasion':'Leader: +Evasion',
        'Leader: +Mastery':'Leader: +Mastery',
        'Leader: +Max Health':'Leader: +Max Health',
        'Leader: +Max Protection':'Leader: +Max Protection',
        'Leader: +Offense':'Leader: +Offense',
        'Leader: +Potency':'Leader: +Potency',
        'Leader: +Speed':'Leader: +Speed',
        'Leader: +Tenacity':'Leader: +Tenacity',
        'Leader: -Defense':'Leader: -Defense',
        'Leader: -Potency':'Leader: -Potency',
        'Leader: -Speed':'Leader: -Speed',
        'Leader: Assist':'Leader: Assist',
        'Leader: CD Reduction':'Leader: CD Reduction',
        'Leader: Crit Avoid':'Leader: Crit Avoid',
        'Leader: Protection Up':'Leader: Protection Up',
        'Leader: TM Gain':'Leader: TM Gain',
        'Leader: TMR':'Leader: TMR',
        'Marked':'Marked',
        'Mass Cleanse':'Mass Cleanse',
        'Mass Dispel':'Mass Dispel',
        'Offense Down':'Offense Down',
        'Offense Up':'Offense Up',
        'Passive':'Passive',
        'Perma Death':'Perma Death',
        'Potency Down':'Potency Down',
        'Potency Up':'Potency Up',
        'Pre Taunt':'Pre Taunt',
        'Protection Up':'Protection Up',
        'Revive':'Revive',
        'Shock':'Shock',
        'Speed Down':'Speed Down',
        'Speed Up':'Speed Up',
        'Stagger':'Stagger',
        'Stats Sharing':'Stats Sharing',
        'Stats Stacking':'Stats Stacking',
        'Stealth':'Stealth',
        'Stun':'Stun',
        'Summon':'Summon',
        'TM Gain':'TM Gain',
        'TM Swap':'TM Swap',
        'TMR':'TMR',
        'Target Lock':'Target Lock',
        'Taunt':'Taunt',
        'Tenacity Down':'Tenacity Down',
        'Tenacity Up':'Tenacity Up',
        'Thermal Detonator':'Thermal Detonator',
        'Translation':'Translation',
        'True Damage':'True Damage',
        'Untargetable':'Untargetable',
        'Vulnerable':'Vulnerable',
        # CHARACTERS
        'Aayla Secura':'Aayla Secura',
        'Admiral Ackbar':'Admiral Ackbar',
        'Admiral Piett':'Admiral Piett',
        'Ahsoka Tano':'Ahsoka Tano',
        'Ahsoka Tano (Fulcrum)':'Ahsoka Tano (Fulcrum)',
        'Amilyn Holdo':'Amilyn Holdo',
        'ARC Trooper':'ARC Trooper',
        'Asajj Ventress':'Asajj Ventress',
        'Aurra Sing':'Aurra Sing',
        'B1 Battle Droid':'B1 Battle Droid',
        'B2 Super Battle Droid':'B2 Super Battle Droid',
        'Barriss Offee':'Barriss Offee',
        'Bastila Shan':'Bastila Shan',
        'Bastila Shan (Fallen)':'Bastila Shan (Fallen)',
        'Baze Malbus':'Baze Malbus',
        'BB-8':'BB-8',
        'Biggs Darklighter':'Biggs Darklighter',
        'Bistan':'Bistan',
        'Bo-Katan Kryze':'Bo-Katan Kryze',
        'Boba Fett':'Boba Fett',
        'Bodhi Rook':'Bodhi Rook',
        'Bossk':'Bossk',
        'C-3PO':'C-3PO',
        'Cad Bane':'Cad Bane',
        'Canderous Ordo':'Canderous Ordo',
        'Captain Han Solo':'Captain Han Solo',
        'Captain Phasma':'Captain Phasma',
        'Cara Dune':'Cara Dune',
        'Carth Onasi':'Carth Onasi',
        'Cassian Andor':'Cassian Andor',
        'CC-2224 "Cody"':'CC-2224 "Cody"',
        'Chewbacca':'Chewbacca',
        'Chief Chirpa':'Chief Chirpa',
        'Chief Nebit':'Chief Nebit',
        'Chirrut Imwe':'Chirrut Imwe',
        'Chopper':'Chopper',
        'Clone Sergeant - Phase I':'Clone Sergeant - Phase I',
        'Clone Wars Chewbacca':'Clone Wars Chewbacca',
        'Colonel Starck':'Colonel Starck',
        'Commander Luke Skywalker':'Commander Luke Skywalker',
        'Coruscant Underworld Police':'Coruscant Underworld Police',
        'Count Dooku':'Count Dooku',
        'CT-21-0408 "Echo"':'CT-21-0408 "Echo"',
        'CT-5555 "Fives"':'CT-5555 "Fives"',
        'CT-7567 "Rex"':'CT-7567 "Rex"',
        'Dark Trooper':'Dark Trooper',
        'Darth Malak':'Darth Malak',
        'Darth Maul':'Darth Maul',
        'Darth Nihilus':'Darth Nihilus',
        'Darth Revan':'Darth Revan',
        'Darth Sidious':'Darth Sidious',
        'Darth Sion':'Darth Sion',
        'Darth Traya':'Darth Traya',
        'Darth Vader':'Darth Vader',
        'Dathcha':'Dathcha',
        'Death Trooper':'Death Trooper',
        'Dengar':'Dengar',
        'Director Krennic':'Director Krennic',
        'Droideka':'Droideka',
        'Echo':'Echo',
        'Eeth Koth':'Eeth Koth',
        'Embo':'Embo',
        'Emperor Palpatine':'Emperor Palpatine',
        'Enfys Nest':'Enfys Nest',
        'Ewok Elder':'Ewok Elder',
        'Ewok Scout':'Ewok Scout',
        'Ezra Bridger':'Ezra Bridger',
        'Finn':'Finn',
        'First Order Executioner':'First Order Executioner',
        'First Order Officer':'First Order Officer',
        'First Order SF TIE Pilot':'First Order SF TIE Pilot',
        'First Order Stormtrooper':'First Order Stormtrooper',
        'First Order TIE Pilot':'First Order TIE Pilot',
        'Gamorrean Guard':'Gamorrean Guard',
        'Gar Saxon':'Gar Saxon',
        'Garazeb "Zeb" Orrelios':'Garazeb "Zeb" Orrelios',
        'General Grievous':'General Grievous',
        'General Hux':'General Hux',
        'General Kenobi':'General Kenobi',
        'General Skywalker':'General Skywalker',
        'General Veers':'General Veers',
        'Geonosian Brood Alpha':'Geonosian Brood Alpha',
        'Geonosian Soldier':'Geonosian Soldier',
        'Geonosian Spy':'Geonosian Spy',
        'Grand Admiral Thrawn':'Grand Admiral Thrawn',
        'Grand Master Yoda':'Grand Master Yoda',
        'Grand Moff Tarkin':'Grand Moff Tarkin',
        'Greedo':'Greedo',
        'Greef Karga':'Greef Karga',
        'Han Solo':'Han Solo',
        'Hera Syndulla':'Hera Syndulla',
        'Hermit Yoda':'Hermit Yoda',
        'HK-47':'HK-47',
        'Hoth Rebel Scout':'Hoth Rebel Scout',
        'Hoth Rebel Soldier':'Hoth Rebel Soldier',
        'Hunter':'Hunter',
        'IG-100 MagnaGuard':'IG-100 MagnaGuard',
        'IG-11':'IG-11',
        'IG-86 Sentinel Droid':'IG-86 Sentinel Droid',
        'IG-88':'IG-88',
        'Ima-Gun Di':'Ima-Gun Di',
        'Imperial Probe Droid':'Imperial Probe Droid',
        'Imperial Super Commando':'Imperial Super Commando',
        'Jango Fett':'Jango Fett',
        'Jawa':'Jawa',
        'Jawa Engineer':'Jawa Engineer',
        'Jawa Scavenger':'Jawa Scavenger',
        'Jedi Consular':'Jedi Consular',
        'Jedi Knight Anakin':'Jedi Knight Anakin',
        'Jedi Knight Guardian':'Jedi Knight Guardian',
        'Jedi Knight Luke Skywalker':'Jedi Knight Luke Skywalker',
        'Jedi Knight Revan':'Jedi Knight Revan',
        'Jedi Master Luke Skywalker':'Jedi Master Luke Skywalker',
        'Jolee Bindo':'Jolee Bindo',
        'Juhani':'Juhani',
        'Jyn Erso':'Jyn Erso',
        'K-2SO':'K-2SO',
        'Kanan Jarrus':'Kanan Jarrus',
        'Ki-Adi-Mundi':'Ki-Adi-Mundi',
        'Kit Fisto':'Kit Fisto',
        'Kuiil':'Kuiil',
        'Kylo Ren':'Kylo Ren',
        'Kylo Ren (Unmasked)':'Kylo Ren (Unmasked)',
        'L3-37':'L3-37',
        'Lando Calrissian':'Lando Calrissian',
        'Lobot':'Lobot',
        'Logray':'Logray',
        'Luke Skywalker (Farmboy)':'Luke Skywalker (Farmboy)',
        'Luminara Unduli':'Luminara Unduli',
        'Mace Windu':'Mace Windu',
        'Magmatrooper':'Magmatrooper',
        'Mission Vao':'Mission Vao',
        'Mob Enforcer':'Mob Enforcer',
        'Moff Gideon':'Moff Gideon',
        'Mon Mothma':'Mon Mothma',
        'Mother Talzin':'Mother Talzin',
        'Nightsister Acolyte':'Nightsister Acolyte',
        'Nightsister Initiate':'Nightsister Initiate',
        'Nightsister Spirit':'Nightsister Spirit',
        'Nightsister Zombie':'Nightsister Zombie',
        'Nute Gunray':'Nute Gunray',
        'Obi-Wan Kenobi (Old Ben)':'Obi-Wan Kenobi (Old Ben)',
        'Old Daka':'Old Daka',
        'Padme Amidala':'Padme Amidala',
        'Pao':'Pao',
        'Paploo':'Paploo',
        'Plo Koon':'Plo Koon',
        'Poe Dameron':'Poe Dameron',
        'Poggle the Lesser':'Poggle the Lesser',
        'Princess Leia':'Princess Leia',
        'Qi\'ra':'Qi\'ra',
        'Qui-Gon Jinn':'Qui-Gon Jinn',
        'R2-D2':'R2-D2',
        'Range Trooper':'Range Trooper',
        'Rebel Officer Leia Organa':'Rebel Officer Leia Organa',
        'Resistance Hero Finn':'Resistance Hero Finn',
        'Resistance Hero Poe':'Resistance Hero Poe',
        'Resistance Pilot':'Resistance Pilot',
        'Resistance Trooper':'Resistance Trooper',
        'Rey':'Rey',
        'Rey (Jedi Training)':'Rey (Jedi Training)',
        'Rey (Scavenger)':'Rey (Scavenger)',
        'Rose Tico':'Rose Tico',
        'Royal Guard':'Royal Guard',
        'Sabine Wren':'Sabine Wren',
        'Savage Opress':'Savage Opress',
        'Scarif Rebel Pathfinder':'Scarif Rebel Pathfinder',
        'Shaak Ti':'Shaak Ti',
        'Shoretrooper':'Shoretrooper',
        'Sith Assassin':'Sith Assassin',
        'Sith Empire Trooper':'Sith Empire Trooper',
        'Sith Eternal Emperor':'Sith Eternal Emperor',
        'Sith Marauder':'Sith Marauder',
        'Sith Trooper':'Sith Trooper',
        'Snowtrooper':'Snowtrooper',
        'Stormtrooper':'Stormtrooper',
        'Stormtrooper Han':'Stormtrooper Han',
        'Sun Fac':'Sun Fac',
        'Supreme Leader Kylo Ren':'Supreme Leader Kylo Ren',
        'T3-M4':'T3-M4',
        'Talia':'Talia',
        'Tech':'Tech',
        'Teebo':'Teebo',
        'The Armorer':'The Armorer',
        'The Mandalorian':'The Mandalorian',
        'The Mandalorian (Beskar Armor)':'The Mandalorian (Beskar Armor)',
        'Threepio & Chewie':'Threepio & Chewie',
        'TIE Fighter Pilot':'TIE Fighter Pilot',
        'Tusken Raider':'Tusken Raider',
        'Tusken Shaman':'Tusken Shaman',
        'Ugnaught':'Ugnaught',
        'URoRRuR'R'R':'URoRRuR'R'R',
        'Vandor Chewbacca':'Vandor Chewbacca',
        'Veteran Smuggler Chewbacca':'Veteran Smuggler Chewbacca',
        'Veteran Smuggler Han Solo':'Veteran Smuggler Han Solo',
        'Visas Marr':'Visas Marr',
        'Wampa':'Wampa',
        'Wat Tambor':'Wat Tambor',
        'Wedge Antilles':'Wedge Antilles',
        'Wicket':'Wicket',
        'Wrecker':'Wrecker',
        'Young Han Solo':'Young Han Solo',
        'Young Lando Calrissian':'Young Lando Calrissian',
        'Zaalbar':'Zaalbar',
        'Zam Wesell':'Zam Wesell',
    },
    {
        'local':'FR-FR',
        # LOCALS
        'EN-US':'English',
        'FR-FR':'Français',
        # COMMANDS
        # Missing arguments
        'missing_arg':'Argument introuvable. Tappez %help pour plus d\'informations.',
        # Local
        'set_local_success':'Nouvelle langue du Bot ',
        'set_local_fail':'Impossible de trouver la langue ',
        # Have
        'have_success':'Personnages avec ',
        'have_fail':'Aucun personnage ne semble interagir avec ',
        # Ability Classes
        'Ability Block':'',
        'Accuracy Down':'',
        'Accuracy Up':'',
        'Advantage':'Avantage',
        'AoE':'',
        'Armor Shred':'',
        'Assist':'',
        'Blind':'Aveuglement',
        'Bonus Attack':'',
        'Bonus Turn':'Tour Bonus',
        'Breach':'Brèche',
        'Buff Immunity':'',
        'Buff Steal':'',
        'Burning':'Brûlure',
        'CD Increase':'',
        'CD Reduction':'',
        'CD Reset':'',
        'Cleanse':'',
        'Confuse':'Confusion',
        'Counter':'Contre-attaque',
        'Crit Chance Down':'',
        'Crit Chance Up':'',
        'Crit Damage Down':'',
        'Crit Damage Up':'',
        'Crit Immunity':'',
        'Damage Immunity':'Immunité aux Dégâts',
        'Daze':'',
        'Deathmark':'Marque de mort',
        'Defense Down':'',
        'Defense Up':'',
        'Dispel':'',
        'DoT':'Dégâts sur la durée',
        'Evasion Down':'',
        'Evasion Up':'',
        'Expose':'',
        'Fear':'Peur',
        'Foresight':'Prévoyance',
        'Frenzy':'Frénésie',
        'Heal':'Soin',
        'Heal Immunity':'Immunité aux soins',
        'Health Down':'',
        'Health Equalization':'Egalisation de vie',
        'Health Up':'',
        'Insta Kill':'Mort Instantannée',
        'Leader: +Counter':'',
        'Leader: +Crit Avoid':'',
        'Leader: +Crit Chance':'',
        'Leader: +Crit Damage':'',
        'Leader: +Defense':'',
        'Leader: +Evasion':'',
        'Leader: +Mastery':'',
        'Leader: +Max Health':'',
        'Leader: +Max Protection':'',
        'Leader: +Offense':'',
        'Leader: +Potency':'',
        'Leader: +Speed':'',
        'Leader: +Tenacity':'',
        'Leader: -Defense':'',
        'Leader: -Potency':'',
        'Leader: -Speed':'',
        'Leader: Assist':'',
        'Leader: CD Reduction':'',
        'Leader: Crit Avoid':'',
        'Leader: Protection Up':'',
        'Leader: TM Gain':'',
        'Leader: TMR':'',
        'Marked':'Marqué',
        'Mass Cleanse':'',
        'Mass Dispel':'',
        'Offense Down':'',
        'Offense Up':'',
        'Passive':'Passif',
        'Perma Death':'Mort permanente',
        'Potency Down':'',
        'Potency Up':'',
        'Pre Taunt':'',
        'Protection Up':'',
        'Revive':'',
        'Shock':'Choc',
        'Speed Down':'',
        'Speed Up':'',
        'Stagger':'',
        'Stats Sharing':'',
        'Stats Stacking':'',
        'Stealth':'Camouflage',
        'Stun':'Etourdissement',
        'Summon':'Invocation',
        'TM Gain':'',
        'TM Swap':'',
        'TMR':'',
        'Target Lock':'',
        'Taunt':'Provocation',
        'Tenacity Down':'',
        'Tenacity Up':'',
        'Thermal Detonator':'Détonateur thermique',
        'Translation':'Traduction',
        'True Damage':'',
        'Untargetable':'Inciblable',
        'Vulnerable':'',
        # CHARACTERS
        'Aayla Secura':'Aayla Secura',
        'Admiral Ackbar':'Amiral Ackbar',
        'Admiral Piett':'Amiral Piett',
        'Ahsoka Tano':'Ahsoka Tano',
        'Ahsoka Tano (Fulcrum)':'Ahsoka Tano (Fulcrum)',
        'Amilyn Holdo':'Amilyn Holdo',
        'ARC Trooper':'',
        'Asajj Ventress':'Asajj Ventress',
        'Aurra Sing':'Aurra Sing',
        'B1 Battle Droid':'',
        'B2 Super Battle Droid':'',
        'Barriss Offee':'Barriss Offee',
        'Bastila Shan':'Bastilla Shan',
        'Bastila Shan (Fallen)':'Bastilla Shan (Déchue)',
        'Baze Malbus':'Baze Malbus',
        'BB-8':'BB-8',
        'Biggs Darklighter':'Biggs Darklighter',
        'Bistan':'Bistan',
        'Bo-Katan Kryze':'Bo-Katan Kryze',
        'Boba Fett':'Boba Fett',
        'Bodhi Rook':'Bodhi Rook',
        'Bossk':'Bossk',
        'C-3PO':'C-3PO',
        'Cad Bane':'Cad Bane',
        'Canderous Ordo':'Canderous Ordo',
        'Captain Han Solo':'Capitaine Han Solo',
        'Captain Phasma':'Capitaine Phasma',
        'Cara Dune':'Cara Dune',
        'Carth Onasi':'Carth Onasi',
        'Cassian Andor':'Cassian Andor',
        'CC-2224 "Cody"':'CC-2224 "Cody"',
        'Chewbacca':'Chewbacca',
        'Chief Chirpa':'Chef Chirpa',
        'Chief Nebit':'Chef Nebit',
        'Chirrut Imwe':'Chirrut Imwe',
        'Chopper':'Chopper',
        'Clone Sergeant - Phase I':'Clone Sergent - Phase I',
        'Clone Wars Chewbacca':'',
        'Colonel Starck':'Colonel Starck',
        'Commander Luke Skywalker':'Commandant Luke Skywalker',
        'Coruscant Underworld Police':'',
        'Count Dooku':'Compte Dooku',
        'CT-21-0408 "Echo"':'CT-21-0408 "Echo"',
        'CT-5555 "Fives"':'CT-5555 "Fives"',
        'CT-7567 "Rex"':'CT-7567 "Rex"',
        'Dark Trooper':'',
        'Darth Malak':'Dark Malak',
        'Darth Maul':'Dark Maul',
        'Darth Nihilus':'Dark Nihilus',
        'Darth Revan':'Dark Revan',
        'Darth Sidious':'Dark Sidious',
        'Darth Sion':'Dark Sion',
        'Darth Traya':'Dark Traya',
        'Darth Vader':'Dark Vador',
        'Dathcha':'Datcha',
        'Death Trooper':'',
        'Dengar':'Dengar',
        'Director Krennic':'Directeur Krennic',
        'Droideka':'Droideka',
        'Echo':'Echo',
        'Eeth Koth':'Eeth Koth',
        'Embo':'Embo',
        'Emperor Palpatine':'Empereur Palpatine',
        'Enfys Nest':'Enfys Nest',
        'Ewok Elder':'',
        'Ewok Scout':'',
        'Ezra Bridger':'Ezra Bridger',
        'Finn':'Finn',
        'First Order Executioner':'',
        'First Order Officer':'',
        'First Order SF TIE Pilot':'',
        'First Order Stormtrooper':'',
        'First Order TIE Pilot':'',
        'Gamorrean Guard':'Garde Gamoréen',
        'Gar Saxon':'Gar Saxon',
        'Garazeb "Zeb" Orrelios':'Garazeb "Zeb" Orrelios',
        'General Grievous':'Général Grievous',
        'General Hux':'Général Hux',
        'General Kenobi':'Général Kenobi',
        'General Skywalker':'Général Skywalker',
        'General Veers':'Général Veers',
        'Geonosian Brood Alpha':'',
        'Geonosian Soldier':'Soldat Géonosien',
        'Geonosian Spy':'Espion Géonosien',
        'Grand Admiral Thrawn':'Grand Amiral Thrawn',
        'Grand Master Yoda':'Grand Maitre Yoda',
        'Grand Moff Tarkin':'Grand Moff Tarkin',
        'Greedo':'Greedo',
        'Greef Karga':'Greef Karga',
        'Han Solo':'Han Solo',
        'Hera Syndulla':'Hera Syndulla',
        'Hermit Yoda':'Yoda Hermite',
        'HK-47':'HK-47',
        'Hoth Rebel Scout':'',
        'Hoth Rebel Soldier':'',
        'Hunter':'Hunter',
        'IG-100 MagnaGuard':'',
        'IG-11':'IG-11',
        'IG-86 Sentinel Droid':'',
        'IG-88':'IG-88',
        'Ima-Gun Di':'Ima-Gun Di',
        'Imperial Probe Droid':'',
        'Imperial Super Commando':'',
        'Jango Fett':'Jango Fett',
        'Jawa':'Jawa',
        'Jawa Engineer':'Ingénieur Jawa',
        'Jawa Scavenger':'',
        'Jedi Consular':'Jedi Consulaire',
        'Jedi Knight Anakin':'Chevalier Jedi Anakin',
        'Jedi Knight Guardian':'Chevalier Jedi Gardien',
        'Jedi Knight Luke Skywalker':'Chevalier Jedi Luke Skywalker',
        'Jedi Knight Revan':'Chevalier Jedi Revan',
        'Jedi Master Luke Skywalker':'Maitre Jedi Luke Skywalker',
        'Jolee Bindo':'Jolee Bindo',
        'Juhani':'Juhani',
        'Jyn Erso':'Jyn Erso',
        'K-2SO':'K-2SO',
        'Kanan Jarrus':'Kanan Jarrus',
        'Ki-Adi-Mundi':'Ki-Adi-Mundi',
        'Kit Fisto':'Kit Fisto',
        'Kuiil':'Kuiil',
        'Kylo Ren':'Kylo Ren',
        'Kylo Ren (Unmasked)':'',
        'L3-37':'L3-37',
        'Lando Calrissian':'Lando Calrissian',
        'Lobot':'Lobot',
        'Logray':'Logray',
        'Luke Skywalker (Farmboy)':'',
        'Luminara Unduli':'Luminara Unduli',
        'Mace Windu':'Mace Windu',
        'Magmatrooper':'',
        'Mission Vao':'Mission Vao',
        'Mob Enforcer':'',
        'Moff Gideon':'Moff Gideon',
        'Mon Mothma':'Mon Mothma',
        'Mother Talzin':'',
        'Nightsister Acolyte':'',
        'Nightsister Initiate':'',
        'Nightsister Spirit':'',
        'Nightsister Zombie':'',
        'Nute Gunray':'Nute Gunray',
        'Obi-Wan Kenobi (Old Ben)':'Obi-Wan Kenobi (Vieux Ben)',
        'Old Daka':'Vieille Daka',
        'Padme Amidala':'Padme Amidala',
        'Pao':'Pao',
        'Paploo':'Paploo',
        'Plo Koon':'Plo Koon',
        'Poe Dameron':'Poe Dameron',
        'Poggle the Lesser':'',
        'Princess Leia':'Princesse Leia',
        'Qi\'ra':'Qi\'ra',
        'Qui-Gon Jinn':'Qui-Gon Jinn',
        'R2-D2':'R2-D2',
        'Range Trooper':'',
        'Rebel Officer Leia Organa':'',
        'Resistance Hero Finn':'',
        'Resistance Hero Poe':'',
        'Resistance Pilot':'',
        'Resistance Trooper':'',
        'Rey':'Rey',
        'Rey (Jedi Training)':'',
        'Rey (Scavenger)':'',
        'Rose Tico':'Rose Tico',
        'Royal Guard':'Garde Royal',
        'Sabine Wren':'Sabine Wren',
        'Savage Opress':'Savage Opress',
        'Scarif Rebel Pathfinder':'',
        'Shaak Ti':'Shaak\'Ti',
        'Shoretrooper':'',
        'Sith Assassin':'',
        'Sith Empire Trooper':'',
        'Sith Eternal Emperor':'',
        'Sith Marauder':'Maraudeur Sith',
        'Sith Trooper':'',
        'Snowtrooper':'',
        'Stormtrooper':'',
        'Stormtrooper Han':'',
        'Sun Fac':'Sun Fac',
        'Supreme Leader Kylo Ren':'',
        'T3-M4':'T3-M4',
        'Talia':'Talia',
        'Tech':'Tech',
        'Teebo':'Teebo',
        'The Armorer':'L\'Armurière',
        'The Mandalorian':'Le Mandalorien',
        'The Mandalorian (Beskar Armor)':'',
        'Threepio & Chewie':'',
        'TIE Fighter Pilot':'',
        'Tusken Raider':'',
        'Tusken Shaman':'Chaman Tusken',
        'Ugnaught':'Ugnaught',
        'URoRRuR'R'R':'URoRRuR'R'R',
        'Vandor Chewbacca':'',
        'Veteran Smuggler Chewbacca':'',
        'Veteran Smuggler Han Solo':'',
        'Visas Marr':'Visas Marr',
        'Wampa':'Wampa',
        'Wat Tambor':'Wat Tambor',
        'Wedge Antilles':'Wedge Antilles',
        'Wicket':'Wicket',
        'Wrecker':'Wrecker',
        'Young Han Solo':'',
        'Young Lando Calrissian':'',
        'Zaalbar':'Zaalbar',
        'Zam Wesell':'Zam Wesell',
    }
]

LOCALS = {
    EN_US:LOCALIZATIONS[0],
    FR_FR:LOCALIZATIONS[1],
}

HELP_LOCAL = {
    # Local
    'local_brief':'Set bot local',
    'local_help':'Set bot localisation.',
    # Who
    'who_brief':'Returns a Character.',
    'who_help':'Returns a Character.',
    # Basic
    'basic_brief':'Returns the Basic Ability of a specified Character.',
    'basic_help':'Returns the Basic Ability of a specified Character.',
    # Kit
    'kit_brief':'Returns all the Abilities of a specified Character.',
    'kit_help':'Returns all the Abilities of a specified Character.',
    # Have
    'have_brief':'Who interacts with a specified Status Effect.',
    'have_help':'Returns a List of Characters that have an interaction with the specified Status Effect.',
    }
