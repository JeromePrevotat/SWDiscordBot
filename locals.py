EN_US = 'EN-US'
FR_FR = 'FR-FR'

LOCALIZATIONS = [
    {
        'local':'EN-US',
        # COMMANDS
        # Local
        'set_local_success':'Bot new local set to ',
        'set_local_fail':'Could not find local ',
        # Have
        'have_fail':'No Character seems to interact with ',
    },
    {
        'local':'FR-FR',
        # COMMANDS
        # Local
        'set_local_success':'Nouvelle langue du Bot  ',
        'set_local_fail':'Impossible de trouver la langue ',
        # Have
        'have_fail':'Aucun personnage ne semble interagir avec ',
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
    'have_help':'Returns a List of Characters that have an interaction \
    with the specified Status Effect.',
    }
