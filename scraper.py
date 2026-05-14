from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_company_details(driver, url):
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except:
        pass

    try:
        page_text = driver.find_element(By.TAG_NAME, "body").text
    except:
        page_text = ""

    description = page_text[:400]

    website = ""
    links = driver.find_elements(By.TAG_NAME, "a")

    for l in links:
        href = l.get_attribute("href")
        if href and "http" in href and "mapyourshow" not in href:
            website = href
            break

    return description, website


def scrape_exhibitors():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://camx2026.mapyourshow.com/8_0/explore/exhibitor-gallery.cfm?featured=false")

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "a"))
    )

    import time

    # Scroll more aggressively
    for _ in range(15):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    exhibitors = []

    links = driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'exhibitor-details')]"
    )

    # Collect unique exhibitor links first
    unique_links = []
    seen = set()

    for link in links:
        href = link.get_attribute("href")
        name = link.text.strip()

        if href and href not in seen and name:
            unique_links.append((name, href))
            seen.add(href)

    print("Collected links:", len(unique_links))

    # Visit each exhibitor page
    for name, href in unique_links[:15]:

        desc, website = get_company_details(driver, href)

        exhibitors.append({
            "name": name,
            "profile_url": href,
            "description": desc,
            "website": website
        })

    driver.quit()

    return exhibitors