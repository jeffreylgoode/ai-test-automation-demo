import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_login_valid_credentials(page: Page):
    page.goto("https://demo-app/login")
    page.fill("#username", "valid_user")
    page.fill("#password", "valid_password")
    page.click("#login")
    expect(page.locator("#dashboard")).to_be_visible()
