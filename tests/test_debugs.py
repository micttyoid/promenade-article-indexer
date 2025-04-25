import pytest

#  mock_print, fxt_print_debug, reload_module_debugs


def test_print_debug_initialization(fxt_print_debug):
    """Test class character"""
    assert isinstance(fxt_print_debug.debug, bool)


def test_print_debug_calls(fxt_print_debug, mock_print):
    """Test format"""
    msg = "hello"
    fxt_print_debug(msg)

    if fxt_print_debug.debug:
        mock_print.assert_called_once_with("DEBUG:", msg)
    else:
        mock_print.assert_not_called()


def test_print_debug_singleton(reload_module_debugs, mock_print):
    """Test print_debug single"""
    # Print when DEBUG=True
    module_debugs = reload_module_debugs(True)
    module_debugs.print_debug("foo")
    mock_print.assert_called_once_with("DEBUG:", "foo")

    # Reset
    mock_print.reset_mock()

    # Not print when DEBUG=False
    module_debugs = reload_module_debugs(False)
    module_debugs.print_debug("bar")
    mock_print.assert_not_called()
