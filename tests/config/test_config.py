from unittest import TestCase

import pydantic

from birpm.config import Config


class ConfigTest(TestCase):
    """Config test"""

    def test_config(self):
        """test config initalization"""
        Config()

    def test_config_verify_hash_algorithms(self):
        with self.assertRaises(pydantic.ValidationError):
            Config(hash_algorithms=[])
        with self.assertRaises(pydantic.ValidationError):
            Config(hash_algorithms=["nonexistant_algorithm"])
        with self.assertRaises(pydantic.ValidationError):
            Config(hash_algorithms=["sha256", "nonexistant_algorithm"])
