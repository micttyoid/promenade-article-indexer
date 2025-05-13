import unittest
from article_indexer.config import Config, config
from article_indexer.utils.debugs import PrintDebug
from unittest.mock import patch
import time
from threading import Thread
import weakref


class TestPrintDebug(unittest.TestCase):
    def setUp(self):
        Config.reset()
        self.printer = PrintDebug()
        config.DEBUG = False

    def tearDown(self):
        if hasattr(self, "printer"):
            if hasattr(self.printer, "_handle_config_change"):
                config.unsubscribe(self.printer._handle_config_change)
            del self.printer
        Config.reset()

    @patch("builtins.print")
    def test_basic_direct_control(self, mock_print):
        self.printer("test1")
        mock_print.assert_not_called()
        self.printer._debug_enabled = True
        self.printer("test2")
        mock_print.assert_called_once_with("[DEBUG]", "test2")
        mock_print.reset_mock()
        self.printer._debug_enabled = False
        self.printer("test3")
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_manual_callback_trigger(self, mock_print):
        self.printer("test1")
        mock_print.assert_not_called()
        self.printer._handle_config_change("DEBUG", False, True)
        self.printer("test2")
        mock_print.assert_called_once_with("[DEBUG]", "test2")
        mock_print.reset_mock()
        self.printer._handle_config_change("DEBUG", True, False)
        self.printer("test3")
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_config_change_with_delay(self, mock_print):
        self.printer("test1")
        mock_print.assert_not_called()
        config.DEBUG = True
        time.sleep(0.1)
        self.printer("test2")
        mock_print.assert_called_once_with("[DEBUG]", "test2")
        mock_print.reset_mock()
        config.DEBUG = False
        time.sleep(0.1)
        self.printer("test3")
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_threaded_config_change(self, mock_print):
        def change_config():
            time.sleep(0.1)
            config.DEBUG = True

        t = Thread(target=change_config)
        t.start()
        self.printer("test1")
        mock_print.assert_not_called()
        t.join()
        self.printer("test2")
        mock_print.assert_called_once_with("[DEBUG]", "test2")

    @patch("builtins.print")
    def test_multiple_instances(self, mock_print):
        printer2 = PrintDebug()
        config.DEBUG = True
        self.printer("test1")
        printer2("test2")
        self.assertEqual(
            mock_print.call_args_list,
            [
                unittest.mock.call("[DEBUG]", "test1"),
                unittest.mock.call("[DEBUG]", "test2"),
            ],
        )
        # Cleanup for second instance
        config.unsubscribe(printer2._handle_config_change)
        del printer2

    @patch("builtins.print")
    def test_content_validation(self, mock_print):
        test_data = ["simple string", 42, {"key": "value"}, ["list", "of", "items"]]
        config.DEBUG = True
        for item in test_data:
            self.printer(item)
        for i, item in enumerate(test_data):
            self.assertEqual(
                mock_print.call_args_list[i], unittest.mock.call("[DEBUG]", item)
            )

    @patch("builtins.print")
    def test_rapid_state_changes(self, mock_print):
        for i in range(50):
            config.DEBUG = bool(i % 2)
            self.printer(f"test{i}")
        printed = [int(call.args[1][4:]) for call in mock_print.call_args_list]
        self.assertTrue(all(x % 2 == 1 for x in printed))

    def test_memory_safety(self):
        ref = weakref.ref(self.printer)
        self.assertIn(self.printer._handle_config_change, config._observers)
        config.unsubscribe(self.printer._handle_config_change)
        del self.printer
        self.assertIsNone(ref())
        self.assertNotIn(PrintDebug._handle_config_change, config._observers)
