
import pytest
from playwright.sync_api import sync_playwright
import time

def test_login_flow_llm_brittle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        # Force a short timeout so the browser closes quickly
        page.set_default_timeout(2000)  # 2 seconds per step

        start = time.time()
        try:
            # LLM-generated (simulated) code — intentionally brittle
            page.goto("https://ai-test-automation-demo.onrender.com/login")

            page.fill("#user", "demo")
            page.fill("input[name='pass']", "password123")
            page.click(".btn-primary")
            page.wait_for_selector(".dashboard-header")

        finally:
            # Ensure browser closes after ~7 seconds max
            elapsed = time.time() - start
            remaining = max(0, 7 - elapsed)
            time.sleep(remaining)
            browser.close()
