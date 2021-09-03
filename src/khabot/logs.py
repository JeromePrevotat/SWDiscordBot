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

def mkdir_log_dir(path):
    """Creates the Logs Directory if it doesn't exists already."""
    if not os.path.exists(path):
        os.mkdir(path, 0o644)

def new_log_file(filename, path):
    """Creates a new empty LogFile."""
    with open(os.path.join(path, filename), 'w+') as f:
        f.write('')

def add_to_log(input, path):
    """Appends the given Input to Today's Log File.
    Creates it if it doesn't exists."""
    today = dt.date.today()
    filename = today.isoformat()
    logline = dt.datetime.now().time().isoformat(timespec='seconds')
    logline += ': ' + input + '\n'
    if not os.path.exists(os.path.join(path, filename)):
        new_log_file(filename, path)
    with open(os.path.join(path, filename), 'a+') as f:
        f.write(logline)

def get_most_recent_logfile(path):
    logFiles = os.listdir(path)
    if len(logFiles) > 0:
        logFiles = [dt.date.fromisoformat(f) for f in logFiles]
        logFiles = sorted(logFiles, reverse=True)
        return logFiles[0].isoformat()
    return None

def get_last_log(path, filename):
    """Returns the last Entry of the most recent Log File."""
    lastLine = ''
    if os.path.exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename)) as f:
            line = f.readline()
            while line:
                lastLine = line
                line = f.readline()
    return lastLine

def purge_old_logs(path):
    """Deletes 7 days old Log Files.
    If any Error is encountered, appends it to the Log File."""
    today = dt.date.today()
    filename = today.isoformat()
    aWeekOld = today - dt.timedelta(days = 7)
    if os.path.exists(path):
        for f in os.listdir(path):
            fileDate = dt.date.fromisoformat(f)
            if fileDate < aWeekOld:
                try:
                    os.remove(os.path.join(path, f))
                except OSError as e:
                    input = 'purge_old_logs: {} {}'.format(e, os.path.join(
                        path, f))
                    add_to_log(input)
