from unittest import TestCase

from main import AGTester


class TestAGTester(TestCase):

    def test_agtester(self):
        AGT = AGTester("Fred")
        self.assertEquals("Autotest with name Fred",AGT.__repr__())
