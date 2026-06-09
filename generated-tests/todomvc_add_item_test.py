from playwright.async_api import async_playwright, expect
import asyncio

async def test_todomvc_add_item():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.playwright.dev/todomvc")

        await page.fill("input.new-todo", "buy milk")
        await page.press("input.new-todo", "Enter")
        await expect(page.locator(".todo-list li")).to_be_visible()

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_todomvc_add_item())