import asyncio
from playwright.async_api import async_playwright, expect

async def test_login_success_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/login")
        await page.fill('input[name="username"]', 'demo')
        await page.fill('input[name="password"]', 'password123')
        await page.click('button[type="submit"]')
        await expect(page.locator('h1')).to_be_visible()

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_login_success_test())