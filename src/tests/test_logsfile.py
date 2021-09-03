###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import unittest
import datetime as dt

import khabot

###############################################################################
#                         CLASS                                               #
###############################################################################

class TestLogsFile(unittest.TestCase):
    """Tests Logs file CRUD."""

    def setUp(self):
        # var SetUp
        self.testDir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        self.logsDirName = 'logs'
        self.logsDir = os.path.join(self.testDir, self.logsDirName)
        self.prefix = khabot.bot.PREFIX
        #self.testBot = khabot.bot.KhaBot()
        self.cmdList = [
        'effects', 'have', 'local', 'help',
        ]
        # Setup a new empty clean Logs Directory
        if not os.path.exists(self.logsDir):
            os.mkdir(self.logsDir, 0o644)
        elif (os.access(self.logsDir, os.W_OK)
            and os.access(self.logsDir, os.R_OK)):
            self.cleanDir(self.logsDir)

    def tearDown(self):
        self.cleanDir(self.logsDir)

    def create_file(self, path, filename, mode):
        try:
            with open(os.path.join(path, filename), mode) as f:
                f.write('')
        except OSError as e:
            print('{}\n -> {}'.format(os.path.join(
                path, filename), e))

    def cleanDir(self, path):
        if os.listdir(path) != []:
            for f in os.listdir(path):
                try:
                    if not os.path.isdir(os.path.join(path, f)):
                        os.remove(os.path.join(path, f))
                except OSError as e:
                    print('{}\n -> {}'.format(os.path.join(path, f), e))

    def populate_dummies_files(self):
        today = dt.date.today()
        # Populate this past Week
        for i in range(1,7):
            filename = (today - dt.timedelta(days = i)).isoformat()
            self.create_file(self.logsDir, filename, 'w+')
        # Populate a Year and a Month ago
        filename = (today - dt.timedelta(days = 32)).isoformat()
        self.create_file(self.logsDir, filename, 'w+')
        filename = (today - dt.timedelta(days = 366)).isoformat()
        self.create_file(self.logsDir, filename, 'w+')
        # Populate a Year and a Month from now
        filename = (today + dt.timedelta(days = 32)).isoformat()
        self.create_file(self.logsDir, filename, 'w+')
        filename = (today + dt.timedelta(days = 366)).isoformat()
        self.create_file(self.logsDir, filename, 'w+')

    def test_create_logs_dir(self):
        """Tests the correct creation of the logs directory."""
        # Mkdir Here
        if os.path.exists(self.logsDir):
            try:
                os.rmdir(self.logsDir)
            except OSError as e:
                print(e)
        khabot.logs.mkdir_log_dir(self.logsDir)
        self.assertTrue(self.logsDirName in os.listdir(self.testDir))

    def test_file_naming(self):
        """Tests the correct naming of logs files."""
        self.cleanDir(self.logsDir)
        fileName = dt.date.today().isoformat()
        # Create File Here
        khabot.logs.new_log_file(fileName, self.logsDir)
        fileList = os.listdir(self.logsDir)
        self.assertTrue(fileList[0], fileName)

    def test_file_content(self):
        """Tests the correct formatting of the log file content."""
        fileOutput = ''
        ref = ''
        filename = dt.datet.today().isoformat()
        # Fill Log File Here
        for cmd in self.cmdList:
            header = dt.datetime.now().time()
            header = header.isoformat(timespec='seconds') + ': ' + self.prefix
            if cmd == 'effects':
                ref += ' '.join([header, cmd]) + '\n'
                khabot.logs.add_to_log(
                    ' '.join([self.prefix, cmd]), self.logsDir)
            if cmd == 'have':
                ref += ' '.join([header, cmd, 'arg1', 'arg2']) + '\n'
                khabot.logs.add_to_log(
                    ' '.join([self.prefix, cmd, 'arg1', 'arg2']), self.logsDir)
            if cmd == 'local':
                ref += ' '.join([header, cmd, 'arg1']) + '\n'
                khabot.logs.add_to_log(
                    ' '.join([self.prefix, cmd, 'arg1']), self.logsDir)
            if cmd not in ['effects', 'have', 'local']:
                ref += ' '.join([header, cmd]) + '\n'
                khabot.logs.add_to_log(
                    ' '.join([self.prefix, cmd]), self.logsDir)
        with open(os.path.join(self.logsDir, filename)) as f:
            line = f.readline()
            while line:
                fileOutput += line
                line = f.readline()
        self.assertEqual(fileOutput, ref)

    def test_delete_old_files(self):
        """Tests the correct Deletion of File older than 7 days."""
        today = dt.date.today()
        aWeekOld = today - dt.timedelta(days = 7)
        # Populate with Dummies Files
        self.populate_dummies_files()
        # Ref
        filesToKeep = []
        for f in os.listdir(self.logsDir):
            if dt.date.fromisoformat(f) > aWeekOld:
                filesToKeep.append(f)
        # Delete Files Here
        khabot.logs.purge_old_logs(self.logsDir)
        self.assertEqual(os.listdir(self.logsDir), filesToKeep)

    def test_get_last_log(self):
        """Tests the correct retrieval of the most recent line in logs."""
        filename = dt.date.today().isoformat()
        correctLine = ''
        lastLine = khabot.bot.get_last_log(filename)
        self.assertEqual(lastLine, correctLine)

    def test_get_most_recent_logfile(self):
        self.populate_dummies_files()
        today = dt.date.today()
        correctFile = (today + dt.timedelta(days = 366)).isoformat()
        # Test non empty Directory
        mostRecentLogFile = khabot.logs.get_most_recent_logfile(self.logsDir)
        self.assertEqual(mostRecentLogFile, correctFile)
        # Test with an empty Directory
        self.cleanDir(self.logsDir)
        mostRecentLogFile = khabot.logs.get_most_recent_logfile(self.logsDir)
        self.assertEqual(mostRecentLogFile, None)

if __name__ == '__main__':
    unittest.main()
