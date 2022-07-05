"""Test Template."""

import pytest

from alexei_lib.terraform.templates.terraform_project import CLIENT, OUTPUT


@pytest.mark.unit
def test_terraform_template():
    """Validate package is importable"""
    assert CLIENT
    assert OUTPUT
