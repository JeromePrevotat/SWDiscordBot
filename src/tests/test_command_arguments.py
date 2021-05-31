###############################################################################
#                         IMPORTS                                             #
###############################################################################

import unittest
import khabot

###############################################################################
#                         CLASS                                               #
###############################################################################

class TestGetCmdArg(unittest.TestCase):
    """Tests Command Arguments Parsing."""
    def setUp(self):
        self.prefix = khabot.bot.PREFIX
        self.testBot = khabot.bot.KhaBot()
        self.cmdList = [
            'effects', 'have', 'local', 'help',
        ]
        self.oneWordArg = 'yolo'
        self.manyWordArg = 'yolo1 yolo2 yolo3 this make no sens at all !'

    def test_command_without_args_nor_options(self):
        for cmd in self.cmdList:
            testCmd = self.prefix + ' ' + cmd
            rCmd, rArgList, rOptList = self.testBot.get_cmd_arg(testCmd)
            self.assertEqual(rCmd, testCmd)
            self.assertEqual(rArgList, None)
            self.assertEqual(rOptList, None)

    def test_command_wih_one_word_arg_no_option(self):
        for cmd in self.cmdList:
            testCmd = ' '.join([self.prefix, cmd, self.oneWordArg])
            rCmd, rArgList, rOptList = self.testBot.get_cmd_arg(testCmd)
            self.assertEqual(rCmd, self.prefix + ' ' + cmd)
            self.assertEqual(rArgList, [self.oneWordArg])
            self.assertEqual(rOptList, None)

    def test_command_wih_many_words_arg_no_option(self):
        for cmd in self.cmdList:
            testCmd = ' '.join([self.prefix, cmd, self.manyWordArg])
            rCmd, rArgList, rOptList = self.testBot.get_cmd_arg(testCmd)
            self.assertEqual(rCmd, self.prefix + ' ' + cmd)
            self.assertEqual(
                rArgList, [w for w in self.manyWordArg.split(sep=' ')])
            self.assertEqual(rOptList, None)

if __name__ == '__main__':
    unittest.main()
