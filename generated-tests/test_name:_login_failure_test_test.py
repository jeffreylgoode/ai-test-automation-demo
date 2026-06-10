from playwright.async_api import async_playwright, expect
import asyncio

async def test_test_name:_login_failure_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/login")
        await page.click("Click the Login button.")
        await expect(page.locator("body")).to_have_text("the error message "Invalid username or password")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_test_name:_login_failure_test())