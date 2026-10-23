import playwright.async_api as playwright
import pytest
from utils.config import  BASE_URL

@pytest.mark.asyncio
async def test_demo(async_page):# webpage load due to of async page
    await async_page.goto(BASE_URL)


#utils method

@pytest.mark.asyncio
async def test_evn_(async_page):
    await async_page.goto(BASE_URL)
    print(await async_page.title())

# how to set up
#python -m venv env
#.venv\script\