import unittest
from unittest.mock import Mock
from article_indexer.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        Config.reset()
        self.config = Config()
        self.mock = Mock()
        self.config.subscribe(self.mock)

    def test_temp_override(self):
        self.config.DEBUG = False
        self.mock.reset_mock()

        with self.config.temporary_config(DEBUG=True):
            self.assertTrue(self.config.DEBUG)
            self.mock.assert_any_call("DEBUG", False, True)

            for call in self.mock.call_args_list:
                self.assertEqual(call.args, ("DEBUG", False, True))

            self.assertGreaterEqual(self.mock.call_count, 1)
            self.assertLessEqual(self.mock.call_count, 2)

    def test_notification_uniqueness(self):
        self.config.DEBUG = False
        self.mock.reset_mock()
        seen_payloads = set()

        def track_payloads(*args):
            seen_payloads.add(args)

        self.mock.side_effect = track_payloads

        with self.config.temporary_config(DEBUG=True):
            self.assertEqual(len(seen_payloads), 1)
            self.assertIn(("DEBUG", False, True), seen_payloads)

    def test_restoration(self):
        self.config.DEBUG = False
        self.mock.reset_mock()

        with self.config.temporary_config(DEBUG=True):
            pass  # Context exits

        self.assertFalse(self.config.DEBUG)
        self.mock.assert_any_call("DEBUG", True, False)

    def tearDown(self):
        Config.reset()
