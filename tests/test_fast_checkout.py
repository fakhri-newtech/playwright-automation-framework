# ==========================================
# FILE: tests/test_fast_checkout.py
# ==========================================
import os
from playwright.sync_api import Page, expect

def test_fast_checkout_with_env(api_logged_in_page: Page):
    
    # 1. We are instantly on the inventory page! Add item and go to cart.
    api_logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    api_logged_in_page.locator(".shopping_cart_link").click()
    
    # 2. Click Checkout
    api_logged_in_page.locator("[data-test='checkout']").click()
    
    # 3. Securely fetch the buyer name from the .env file
    buyer_name = os.getenv("TEST_BUYER")
    
    # 4. Fill the First Name field using the hidden variable
    api_logged_in_page.locator("[data-test='firstName']").fill(buyer_name)
    
    # 5. Assert the field actually contains the value
    expect(api_logged_in_page.locator("[data-test='firstName']")).to_have_value(buyer_name)


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & Review
# (Explain this while reviewing the solution)
# ==========================================
# 1. Integration Check:
#    Ask the students: "Did you notice how fast that was? Your test didn't 
#    type 'standard_user'. It just teleported to the products page, clicked 
#    three times, and typed your name from a hidden file. THIS is how senior 
#    engineers write UI automation."
#
# 2. `buyer_name = os.getenv("TEST_BUYER")`:
#    Remind them: "If someone steals this Python file, they have NO IDEA who 
#    the buyer is, what the URL is, or what the password is. The logic is 
#    completely decoupled from the data. 
#    
# 3. Pre-Break Wrap Up:
#    Tell the students: "Take a 15-minute break. Do not close VS Code. When 
#    we come back, we are going to take this exact, secure, lightning-fast 
#    framework and push it to GitHub."