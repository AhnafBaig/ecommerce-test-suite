"""
UI Tests — Shopping Cart
========================
Binds the BDD scenarios from features/shopping_cart.feature to pytest-bdd.
Step definitions live in steps/ui/cart_steps.py and are imported
globally via the root conftest.py.
"""
from pytest_bdd import scenarios

scenarios("../../features/shopping_cart.feature")
