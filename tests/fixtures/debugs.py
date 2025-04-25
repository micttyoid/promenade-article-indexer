import pytest
from unittest.mock import patch
from article_indexer.utils.debugs import PrintDebug


@pytest.fixture
def mock_print():
    """Mock the print"""
    with patch("builtins.print") as mock:
        yield mock


@pytest.fixture(params=[True, False])
def fxt_print_debug(request):
    """Provide debug states"""
    return PrintDebug(debug=request.param)


@pytest.fixture
def reload_module_debugs():
    """Fixture to help reload the module with new config"""

    def _reload(debug_value):
        with patch("article_indexer.utils.debugs.config.DEBUG", debug_value):
            import importlib
            import article_indexer.utils.debugs

            importlib.reload(article_indexer.utils.debugs)
            return article_indexer.utils.debugs

    return _reload
