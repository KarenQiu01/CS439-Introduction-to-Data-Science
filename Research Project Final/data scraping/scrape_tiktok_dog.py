import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # launch a visible Chromium (so TikTok won’t block you as a bot)
        browser = p.chromium.launch(headless=False)
        page    = browser.new_page()
        
        # go to the #dog tag page
        page.goto("https://www.tiktok.com/tag/dog", timeout=60000)
        # wait until at least one video thumbnail shows up
        page.wait_for_selector('a[href*="/video/"]', timeout=60000)

        # scroll down a few times to load more videos
        for _ in range(8):
            page.mouse.wheel(0, 8000)
            time.sleep(1.5)

        # collect up to 100 unique links
        links = []
        for a in page.query_selector_all('a[href*="/video/"]'):
            href = a.get_attribute("href")
            if href and href.startswith("https://www.tiktok.com/") and href not in links:
                links.append(href)
            if len(links) >= 100:
                break

        browser.close()

    # write out what we found
    with open("tiktok_dog_urls.txt", "w", encoding="utf-8") as f:
        for url in links:
            f.write(url + "\n")

    print(f"Saved {len(links)} URLs to tiktok_dog_urls.txt")

if __name__ == "__main__":
    main()
