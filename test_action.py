import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_freams(async_page):
    await async_page.goto("https://jqueryui.com/datepicker/")

    frame = async_page.frame_locator(".demo-frame")

    await frame.locator("//input[@id='datepicker']").click()
    await frame.locator("//a[text()='14']").click()

    import pytest
    from playwright.async_api import expect

    import pytest
    from playwright.async_api import expect




    @pytest.mark.asyncio
    async def test_file_upload(async_page):
        await async_page.goto("https://practice.expandtesting.com/upload")

        # must be a FILE path, not a folder
        await async_page.locator("#fileInput").set_input_files("C:\\Users\\shrey\\Downloads\\61944481-c832-4b21-9f73-61621ac9f063\\61944481-c832-4b21-9f73-61621ac9f063\\CLIENT")
        await async_page.locator("#fileSubmit").click()

        await expect(async_page.get_by_text("File Uploaded!")).to_be_visible()
         msg = async_page.get_by_text("File Uploaded!")
         await expect(msg).to_be_visible()


@pytest.mark.asyncio
async def test_right_clk(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.locator("//button[text()='Copy Text']").click(button="right")
    await async_page.wait_for_timeout(5000)