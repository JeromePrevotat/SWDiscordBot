###############################################################################
#                         IMPORTS                                             #
###############################################################################

import os
import unittest

import khabot

###############################################################################
#                         CLASS                                               #
###############################################################################

class TestLogsFile(unittest.TestCase):
    """Tests Logs file CRUD."""
    def setUp(self):
        self.testBot = khabot.bot.KhaBot()
        self.cwd = os.getcwd()
        self.dirName = 'logs'
        self.logsFileName = ''

    def test_dir_create(self):
        """Tests the correct creation of the logs directory."""
        self.assertTrue(self.dirName in os.listdir(self.cwd))
