from unittest import TestCase

from birpm.config import Config


class ConfigTest(TestCase):
    """Config test"""

    def test_config(self):
        """test config initalization"""
        Config()
