from playwright.async_api import async_playwright, expect
import asyncio

async def test_test_name:_login_success_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/login")
        await page.click("Click the Login button.")
        await page.goto("/dashboard.")
        await expect(page.locator("the text "Welcome to the Dashboard!" is")).to_be_visible()

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_test_name:_login_success_test())