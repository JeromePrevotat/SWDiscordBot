###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import unittest

import khabot

###############################################################################
#                         CLASS                                               #
###############################################################################

class TestLogsFile(unittest.TestCase):
    """Tests Logs file CRUD."""

    def cleanDir(self, path):
        if os.listdir(path) != []:
            for f in os.listdir(path):
                print(f)
                print(path)
                try:
                    if os.path.isdir(f):
                        cleanDir(os.path.join(path, f))
                    else:
                        os.remove(f)
                except OSError as e:
                    print('{}\n -> {}'.format(os.path.join(path, f), e))
        try:
            os.rmdir(path)
        except OSError as e:
            print('{}\n -> {}'.format(path, e))

    def setUp(self):
        # Var SetUp
        self.testBot = khabot.bot.KhaBot()
        self.fileDir = os.path.dirname(os.path.abspath(__file__))
        self.logsParentDir = os.path.join(self.fileDir, '..')
        self.dirName = 'logs'
        self.logsFileName = ''
        # Dir SetUp
        # Clean and Remove Logs Dir if it exists
        if self.dirName in os.listdir(self.logsParentDir):
            self.cleanDir(os.path.join(self.logsParentDir, self.dirName))

    def test_dir_create(self):
        """Tests the correct creation of the logs directory."""
        self.assertTrue(self.dirName in os.listdir(self.logsParentDir))

if __name__ == '__main__':
    import sys
    print(sys.path)
    t = TestLogsFile()
    p = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'logs')
    t.cleanDir(p)
