from playwright.async_api import async_playwright, expect
import asyncio

async def test_test_name:_dashboard_navigation_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/dashboard")
        await page.fill("#username", "demo")
        await page.fill("#password", "password123")
        await page.click("#login-button")
        await expect(page.locator("the "Back to Home" link is")).to_be_visible()
        await page.click("Click "Back to Home".")
        await page.goto("/.")
        await page.goto("/dashboard")
        await expect(page.locator("the "Logout" link is")).to_be_visible()
        await page.click("Click "Logout".")
        await page.goto("/.")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_test_name:_dashboard_navigation_test())