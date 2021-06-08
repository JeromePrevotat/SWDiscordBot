###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import datetime as dt

#from khabot import bot

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

LOGSDIRNAME = 'logs'
LOGSDIR = os.path.join(os.path.abspath(os.path.dirname(
    os.path.dirname(__file__))), LOGSDIRNAME)

def mkdir_log_dir():
    if not os.path.exists(LOGSDIR):
        os.mkdir(LOGSDIR, 0o644)

def new_log_file(filename):
    with open(os.path.join(LOGSDIR, filename), 'w+') as f:
        f.write('')

def add_to_log(input):
    today = dt.date.today()
    filename = today.isoformat()
    logline = dt.datetime.now().time().isoformat() + ': ' + input + '\n'
    if not os.path.exists(os.path.join(LOGSDIR, filename)):
        new_log_file(filename)
    with open(os.path.join(LOGSDIR, filename), 'a+') as f:
        f.write(input)

def purge_old_logs():
    today = dt.date.today()
    filename = today.isoformat()
    aWeekOld = today - dt.timedelta(days = 7)
    if os.path.exists(LOGSDIR):
        for f in os.listdir(LOGSDIR):
            fileDate = dt.date.fromisoformat(f)
            if fileDate < aWeekOld:
                try:
                    os.remove(os.path.join(LOGSDIR, f))
                except OSError as e:
                    input = 'purge_old_logs: {} {}'.format(e, os.path.join(
                        LOGSDIR, f))
                    add_to_log(input)
