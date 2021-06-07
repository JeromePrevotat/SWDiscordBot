###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import unittest
import datetime

import khabot

###############################################################################
#                         CLASS                                               #
###############################################################################

class TestLogsFile(unittest.TestCase):
    """Tests Logs file CRUD."""

    def setUp(self):
        # Var SetUp
        self.parentDir = os.path.abspath(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
        self.logsDirName = 'logs'
        self.logsDir = os.path.join(os.path.abspath(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))), self.logsDirName)
        self.prefix = khabot.bot.PREFIX
        self.testBot = khabot.bot.KhaBot()
        self.cmdList = [
            'effects', 'have', 'local', 'help',
        ]

    def tearDown(self):
        self.cleanDir(self.logsDir)

    def cleanDir(self, path):
        if os.listdir(path) != []:
            for f in os.listdir(path):
                try:
                    if not os.path.isdir(os.path.join(path, f)):
                        os.remove(os.path.join(path, f))
                        print('RM FILE: {}\n'.format(os.path.join(path, f)))
                except OSError as e:
                    print('{}\n -> {}'.format(os.path.join(path, f), e))

    def test_create_logs_dir(self):
        """Tests the correct creation of the logs directory."""
        # Mkdir Here
        self.assertTrue(self.logsDirName in os.listdir(self.parentDir))

    def test_file_naming(self):
        """Tests the correct naming of logs files."""
        self.cleanDir(self.logsDir)
        correctName = datetime.date.today().isoformat()
        # Create File Here
        fileList = os.listdir(self.logsDir)
        self.assertTrue(fileList[0], correctName)

    def test_file_content(self):
        """Tests the correct formatting of the log file content."""
        mine = ''
        ref = ''
        # Fill Log File Here
        for cmd in self.cmdList:
            header = datetime.datetime.now().time()
            header = header.isoformat(timespec='seconds') + ': ' + self.prefix
            if cmd == 'effects':
                ref +=' '.join([header, cmd, '\n'])
            if cmd == 'have':
                ref += ' '.join([header, cmd, 'arg1', 'arg2', '\n'])
            if cmd == 'local':
                ref += ' '.join([header, cmd, 'arg1', '\n'])
            if cmd not in ['effects', 'have', 'local']:
                ref += ' '.join([header, cmd, '\n'])
        self.assertEqual(mine, ref)

    def test_delete_old_files(self):
        today = datetime.date.today()
        aWeekOld = today - datetime.timedelta(days = 7)
        # Delete Files Here
        self.assertEqual(os.listdir(self.logsDir), [])

if __name__ == '__main__':
    unittest.main()
