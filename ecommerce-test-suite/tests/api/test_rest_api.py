"""
API Tests — REST API
====================
Binds the BDD scenarios from features/api/rest_api.feature to pytest-bdd.
Step definitions live in steps/api/api_steps.py and are imported
globally via the root conftest.py.

Note: The `api_context` fixture is defined in steps/api/api_steps.py and
shared via the conftest import chain — no Playwright browser is needed here.
"""
from pytest_bdd import scenarios

scenarios("../../features/api/rest_api.feature")
