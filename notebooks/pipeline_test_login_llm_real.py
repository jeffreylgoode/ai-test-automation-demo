
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Navigate to /login
    page.goto("https://ai-test-automation-demo.onrender.com/login")

    # 2. Enter username "demo"
    page.fill('input[name="username"]', "demo")

    # 3. Enter password "password123"
    page.fill('input[name="password"]', "password123")

    # 4. Click login button
    page.click('button[type="submit"]')

    # 5. Verify dashboard_heading visible
    page.wait_for_selector('[data-testid="dashboard_heading"]')

    print("Login Success Test Passed")

    browser.close()
