"""Test Template."""

import pytest

from alexei_lib.terraform import bootstrap


@pytest.mark.unit
def test_package():
    """Validate package is importable"""
    bootstrap.bootstrap_terraform_project()
