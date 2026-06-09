from playwright.async_api import async_playwright, expect
import asyncio

async def test_todomvc_add_and_complete_items():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.playwright.dev/todomvc")

        # Unsupported action: input
        # Unsupported action: press
        # Unsupported action: input
        # Unsupported action: press
        # Unsupported action: click
        # Unsupported action: click

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_todomvc_add_and_complete_items())