###############################################################################
#                         CONSTANTS                                           #
###############################################################################

FEATS = {
    # SECTOR 1
    '1':    'Opportunistic Advance : Attack out of Turn 100 times\n\t- CLS/Jedi/Troopers/BH/GG\n\
            Lucky Shot : Score 200 Critical Hits\n\t- Whatever\n\
            Critical Success : Gain Advantage 40 times\n\t- First Order/GMY steal & spread\n\
            Kalikori : Defeat 30 units with Phoenix Squadron units\n\t- JML Wat Ezra Hoda Jolee\n\
            Bounties to Collect : Win at least 14 battles with a full Squad of Bounty Hunter units\n\t- Bossk Mando Greef Jango vs Nightsisters\n\
            Incapacitating Strike : Attempt to inflict Potency Down 40 times\n\t- GMY Basic\n\
            \nMini Boss Padme:\n\
            For the Light : Win with a full Squad of Light Side units\n\t- CLS/JKR GMY\n\
            A Touch of Darkness : Win with a full Squad of Dark Side units\n\t- GG\n\
            Calculated Risk : Complete the battle with an undersized Squad\n\t- JKR GMY Jolee Hoda\n\
            \nBoss QGJ:\n\
            All Separatists : Win with a full Squad of Separatists units\n\t- GG\n\
            Unguarded : Win the battle with no Tanks in your Squad\n\t- JKR JKL GMY Jolee Hoda\n\
            Stunning Tactics : Complete the battle after attempting to inflict Stun 20 times\n\t- JML JKL Aayla GMY Jolee\n',
    # Sector 2
    '2':    'Unsupportive : Win 10 battles with no Supports in your Squad\n\t- CLS Han Chewie Threepio CAT/Fulcrum/Lando\n\
            Best Defense : Win a battle with 5 Attackers in your Squad 10 times\n\t- CLS Han Chewie Threepio CAT/Fulcrum/Lando\n\
            Super Support : Grant at least 100 buffs to allies\n\t- GMY\n\
            All Nightsisters : Win at least 14 battles with a full Squad of Nightsister units\n\t- NS vs Geos\n\
            Striking Back : Defeat 40 units with Rebel Fighter units\n\t- MM Wedge Biggs Lando Cara Dune vs Boss : Zombie farm\n\
            Blinding Assault : Attempt to inflict Blind 40 times\n\t- Threepio\n\
            \nMini Boss GG:\n\
            For the Light : Win with a full Squad of Light Side units\n\t- JKR/Padme\n\
            A Touch of Darkness : Win with a full Squad of Dark Side units\n\t- GG\n\
            Calculated Risk : Complete the battle with an undersized Squad\n\t- JKR GMY Jolee Hoda\n\
            \nBoss : Nightsister:\n\
            Recovery Expert : Recover at least 300.000 points of Health\n\t- JML Wat Zariss Hoda Jolee\n\
            Going Critical : Score at least 20 Critical hits in a row during ally turns\n\t- JKL JKR GMY Bastilla Aayla\n\
            Flawless Victory : Win without loosing any units\n\t- Whatever\n',
    # Sector 3
    '3':    'Stunning Tactics : Inflict Stun 100 times\n\t- JKL/EP\n\
            Shadowy Dealings : Gain Stealth 40 times\n\t- Jedi + Hoda & GMY or Rebels/GR + R2D2 & C3PO\n\
            Relentless Fury : Gain Frenzy 20 times\n\t- Initial Frenzy Tech/JML JKR Hoda Wat Bossk\n\
            All Old Republic : Defeat 40 units with Old Republic units\n\t- JML JKR Hoda Wat Bossk\n\
            Clumsy : Attempt to inflict Evasion Down 40 times\
            All Empire : Win at least 14 battle with a full Squad of Empire units\
            \nMini Boss Bo Katan Mandalorians:\n\
            For the Light : Win with a full Squad of Light Side units\n\t- JML JKR Hoda JKL Gas\n\
            A Touch of Darkness : Win with a full Squad of Dark Side units\n\t- GG\n\
            Calculated Risk : Complete the battle with an undersized Squad\n\t- JML JKR Hoda Wat\n\
            \nBoss : Sidious:\n\
            Hindered Movement : remove from enemies at least 700% Turn Meter (total)\n\t- JML Old Ben JTR C3PO Wat\n\
            Simple Tricks : Win without using more than 6 Special Abilities\n\t- JKL JML Gas Hoda JKR\n\
            You are Under Arrest : Win with mace Windu on your Squad\n\t- JML JKR JKL Mace Windu Hoda\n\
            End of the Jedi : Win without using any Jedi characters in your Squad\n\t- GG\n',
    # Sector 4
    '4':    '? : Evades 100 attacks in battles you won\n\t- Jedi + Hoda & GMY\n\
            ? : Win 10 battles with no Attackers in your Squad\n\t\- JML Zariss GMY Jolee Hoda\n\
            Reeling Blow : Attempt to inflict Stagger 60 times\n\t- JML Hoda Wat Jango BSF\n\
            Tradition of War : Defeat 50 units with Mandalorian units\n\t- JML Hoda Wat Jango BSF\n\
            All Smugglers : Win at least 14 battles with a full Squad of Smugglers\n\t- Skipped\n\
            Evasive Movement : Gain evasion Up 20 times\n\t- Threepio\n\
            \nMini Boss Ahsoka :\n\
            For the Light : Win with a full Squad of Light Side units\n\t- Whatever\n\
            A Touch of Darkness : Win with a full Squad of Dark Side units\n\t- GG\n\
            Calculated Risk : Complete the battle with an undersized Squad\n\t- JML JKR Hoda Wat\n\
            \nBoss : Maul Mandalorian:\n\
            Crack in the Armor : Gain Defense Penetration Up 20 times\n\t- JML GMY JKR Gas Hoda\n\
            Beskar Breaker : inflict Armor Shred 3 times\n\
            Crush Them : Defeat at least 3 enemies in the same turn\n\t- JML JKL Gas JKR Hoda\n\
            Unsupportive : Win without using any Support in your Squad\n\t- CLS\n\',
    # Sector 5
    '5':    'Blow : Inflict Daze 40 times\n\t- JML Gas\n\
            Victory : Defeat at least 100 enemies\n\t- Whatever\n\
            Marked for Death : inflict Deathmark 10 times\n\t- DR Lead/Troopers/JML Wat Deathtrooper\n\
            Flawless Victory : Win at least 20 battles without loosing any units\n\t- JML\n\
            Let\'s Blow Something Up : Defeat 40 units with Bad Batch\n\t- Skipped\n\
            Brood Warfare : Win 14 battles with a full Squad of Geonosian units\n\t- Geo + Overcharged Medpack/Protection/Faction Tech vs Miniboss\n\
            \nMini Boss Phoenix :\n\
            For the Light : Win with a full Squad of Light Side units\n\t- Whatever\n\
            A Touch of Darkness : Win with a full Squad of Dark Side units\n\t- GG\n\
            Calculated Risk : Complete the battle with an undersized Squad\n\t- JML JKR Hoda Wat\n\
            \nBoss : JMK:\n\
            Armor Up : Gain Defense Up 20 times\n\t- JML\n\
            Guarded Assault : Complete the battle without losing a unit while at least one Attacker is in the Squad\n\t- Gas 501rst/JML JKL JKR Hoda Jolee\n\
            Devastating Strike : Deal at least 200.000 damage to an enemy in a single hit\n\t- - Gas 501rst/JML JKL JKR Hoda Jolee\n\
            Opportunistic Advance : Attack out of Turn at least 30 times\n\t- - Gas 501rst/JML JKL JKR Hoda Jolee\n,
    # General Feats
    'g':    'Live in Light : Win 50 battles with a full Squad of Light Side units\
            Dabble in Darkness : Win 50 battles with a full Squad of Dark Side units\
            That\'ll leave a Mark : Gain 500 Offense Up times\
            Grand Victory : Defeat at least 500 enemies\
            Unguarded : Win 20 battles with no Tanks in your squad\
            Nightbrother : Win 20 battles with Darth Maul & Savage Opress\
            One\'s own path : Defeat 100 enemy units in Conquest with Unaligned Force Users',
}
