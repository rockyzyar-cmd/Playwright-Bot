from playwright.sync_api import sync_playwright
import time
import sys

LINK = "https://www.instagram.com/reel/DWN9X_gD3bH/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
SITE = "https://zefame.com/en/free-instagram-views"

def run_cycle():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")

        # Fallback: agar contexts empty hain to naya context banao
        context = browser.contexts[0] if browser.contexts else browser.new_context()

        # Fallback: agar pages empty hain to naya page banao
        page = context.pages[0] if context.pages else context.new_page()

        page.goto(SITE)
        page.wait_for_selector("#instagram-link", timeout=20000)
        page.fill("#instagram-link", LINK)
        page.click("#submit-btn", force=True)

        print("✅ Cycle complete — link submitted.", flush=True)

if __name__ == "__main__":
    while True:
        run_cycle()
        print("⏳ Waiting 400 seconds...", flush=True)

        # Counter loop
        for i in range(1, 400):   # 1 se 400 tak
            print(i, flush=True)   # force log flush for GitHub Actions
            time.sleep(1)          # har second pe print hoga

        # Fir cycle repeat ho jaayega
