"""
UI Tests — Login
================
Binds the BDD scenarios from features/login.feature to pytest-bdd.
Step definitions live in steps/ui/login_steps.py and are imported
globally via the root conftest.py.
"""
import pytest
from pytest_bdd import scenarios

# Register all scenarios from the login feature file
scenarios("../../features/login.feature")
