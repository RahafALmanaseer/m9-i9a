import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from query import execute_query

def test_unknown_intent_exits_non_zero():
    with pytest.raises(SystemExit):
        execute_query("invalid-command")

def test_list_authors_returns_results():
    res = execute_query("list-authors")
    assert "results" in res
