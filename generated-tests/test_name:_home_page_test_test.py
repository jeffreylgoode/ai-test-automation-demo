from playwright.async_api import async_playwright, expect
import asyncio

async def test_test_name:_home_page_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/")
        await expect(page.locator("the heading "Hello from your Flask Demo App!" is")).to_be_visible()
        await expect(page.locator("the "Login" link is")).to_be_visible()
        await page.click("Click the "Login" link.")
        await page.goto("/login.")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_test_name:_home_page_test())