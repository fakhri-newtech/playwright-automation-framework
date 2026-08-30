# ==========================================
# FILE: tests/test_checkout_ai.py
# ==========================================
import pytest
from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage

# AI-Generated Edge Cases Matrix
@pytest.mark.parametrize("first, last, postal, expected_error", [
    ("", "Smith", "12345", "Error: First Name is required"),
    ("John", "", "12345", "Error: Last Name is required"),
    ("John", "Smith", "", "Error: Postal Code is required"),
    ("Drop", "Table", "Users", "Error: Postal Code is required") # Fun AI edge case
])
def test_checkout_errors(logged_in_page: Page, first, last, postal, expected_error):
    # Navigate to checkout
    logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    logged_in_page.locator(".shopping_cart_link").click()
    logged_in_page.locator("[data-test='checkout']").click()
    
    # Use POM to fill the form
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_checkout_info(first, last, postal)
    
    # Assert the exact error message appears
    expect(checkout_page.error_message).to_contain_text(expected_error)