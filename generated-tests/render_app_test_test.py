from playwright.async_api import async_playwright, expect
import asyncio

async def test_render_app_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ai-test-automation-demo.onrender.com/")
        await page.goto("https://ai-test-automation-demo.onrender.com/login")
        await page.click("button[type='submit']")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_render_app_test())