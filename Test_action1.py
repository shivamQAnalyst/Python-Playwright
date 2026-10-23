import pytest
from pathlib import Path
from playwright.async_api import expect


class TestFrames:

    @pytest.mark.asyncio
    async def test_file_upload(self, async_page):
        path = Path(r"C:\Users\shrey\Downloads\61944481-c832-4b21-9f73-61621ac9f063\61944481-c832-4b21-9f73-61621ac9f063\CLIENT")

        # if CLIENT is a folder, upload the first file inside it
        if path.is_dir():
            files = [f for f in path.iterdir() if f.is_file()]
            assert files, f"No files found inside {path}"
            path = files[0]

        print("Uploading:", path)

        await async_page.goto("https://practice.expandtesting.com/upload")
        await async_page.locator("#fileInput").set_input_files(str(path))
        await async_page.locator("#fileSubmit").click()

        await expect(async_page.get_by_text("File Uploaded!")).to_be_visible()


