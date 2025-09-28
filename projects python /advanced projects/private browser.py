# egkatastasi playwright (automata/eseis)

import sys
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://google.com/"
USER_PLAYWRIGHT_PROFILE = Path.home() / ".playwright_user_profile"

def run_visible(cmd):
    if sys.platform == "win32" and hasattr(subprocess, "CREATE_NEW_CONSOLE"):
        return subprocess.run(cmd, check=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
    return subprocess.run(cmd, check=True)

def ensure_playwright_install():
    try:
        import playwright
    except Exception:
        print("Egkatastasi Playwright...")
        run_visible([sys.executable, "-m", "pip", "install", "--user", "playwright"])
    try:
        from playwright._impl._driver import get_driver_executable
        _ = get_driver_executable("chromium")
    except Exception:
        print("Egkatastasi Playwright browsers...")
        run_visible([sys.executable, "-m", "playwright", "install"])

ensure_playwright_install()

with sync_playwright() as p:
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    browser = p.chromium.launch_persistent_context(
        str(USER_PLAYWRIGHT_PROFILE),
        headless=False,
        args=[
            "--force-dark-mode",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-software-rasterizer"
        ],
        viewport={"width": 1280, "height": 900},
        user_agent=ua,
        locale="en-US",
        timezone_id="UTC"
    )
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        browser.close()

