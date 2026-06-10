from playwright.async_api import async_playwright, expect
import asyncio

async def test_test_name:_logout_flow_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/logout")
        await page.fill("#username", "demo")
        await page.fill("#password", "password123")
        await page.click("#login-button")
        await page.click("Click the Logout link.")
        await page.goto("/.")
        await expect(page.locator("the home page heading is")).to_be_visible()

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_test_name:_logout_flow_test())