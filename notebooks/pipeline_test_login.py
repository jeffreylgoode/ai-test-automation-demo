import pytest
from playwright.sync_api import sync_playwright

def test_login_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://ai-test-automation-demo.onrender.com/login")
        page.fill("input[name=\"username\"]", "demo")
        page.fill("input[name=\"password\"]", "password123")
        page.click("button[type=\"submit\"]")
        page.wait_for_selector("h1")
        browser.close()
