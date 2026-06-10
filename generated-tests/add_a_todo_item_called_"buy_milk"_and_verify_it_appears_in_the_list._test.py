from playwright.async_api import async_playwright, expect
import asyncio

async def test_add_a_todo_item_called_"buy_milk"_and_verify_it_appears_in_the_list.():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()


        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_add_a_todo_item_called_"buy_milk"_and_verify_it_appears_in_the_list.())