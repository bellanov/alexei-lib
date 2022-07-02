"""Test Template."""

import pytest

from alexei_lib import alexei


@pytest.mark.unit
def test_package():
    """Validate package is importable"""
    assert alexei.hello_alexei() == "Hello Alexei!"
