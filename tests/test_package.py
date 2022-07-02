"""Test Template."""

import pytest

from alexei_lib import alexei


@pytest.mark.unit
def test_hello():
    """Validate package is importable"""
    assert alexei.hello_world() == "Hello Alexei!"
