# ==========================================
# FILE: tests/test_cart_fixture.py
# ==========================================
from playwright.sync_api import Page, expect

def test_add_to_cart(logged_in_page: Page):
    # Notice we don't need to visit the URL or log in here!
    # The fixture handled it securely.
    
    logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")