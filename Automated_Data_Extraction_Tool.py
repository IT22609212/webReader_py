import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.headless = False



CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_DRIVER_PATH = r"C:\webdriver\chromedriver.exe"

options.binary_location = CHROME_PATH
service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# URL to scrape
url = "https://app.gulfood.com/meet/s/companies/"
driver.get(url)
time.sleep(5)  # Allow time for the page to load

# Open CSV file for saving data
csv_file = "gulfood_companies.csv"
fieldnames = ["Name", "Sponsor", "Location", "Pavilion", "Hall Number", "Country", "Company Type"]

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    processed_ids = set()  # To track processed companies

    while True:
        companies = driver.find_elements(By.CSS_SELECTOR, "ul#attendees li")
        if not companies:
            break

        for company in companies:
            company_id = company.get_attribute("id")
            if company_id in processed_ids:
                continue  # Skip already processed companies

            try:
                # Scroll to the company to ensure it is visible
                driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", company)
                time.sleep(1)

                # Extract details from the company element
                try:
                    name = company.find_element(By.CSS_SELECTOR, "h5#co_name").text
                except:
                    name = "N/A"

                try:
                    sponsor = company.find_element(By.CSS_SELECTOR, "span.p_box").text
                except:
                    sponsor = "N/A"

                try:
                    location = company.find_element(By.CSS_SELECTOR, "span.f12.bold.text-truncate").text
                except:
                    location = "N/A"

                # Click to navigate to the detailed view
                try:
                    wait.until(EC.element_to_be_clickable(company)).click()
                    time.sleep(3)  # Wait for the details to load

                    try:
                        pavilion = driver.find_element(By.XPATH, "//p[text()='Pavilion']/following-sibling::div").text
                    except:
                        pavilion = "N/A"

                    try:
                        hall_number = driver.find_element(By.XPATH, "//p[text()='Hall Number']/following-sibling::div").text
                    except:
                        hall_number = "N/A"

                    try:
                        country = driver.find_element(By.XPATH, "//p[text()='Country']/following-sibling::div").text
                    except:
                        country = "N/A"

                    try:
                        company_type = driver.find_element(By.XPATH, "//p[text()='Company Type']/following-sibling::div").text
                    except:
                        company_type = "N/A"

                    # Write data to CSV and print it
                    data = {
                        "Name": name,
                        "Sponsor": sponsor,
                        "Location": location,
                        "Pavilion": pavilion,
                        "Hall Number": hall_number,
                        "Country": country,
                        "Company Type": company_type,
                    }
                    writer.writerow(data)
                    print(data)

                    # Mark company as processed
                    processed_ids.add(company_id)

                    # Close the details view
                    try:
                        driver.find_element(By.ID, "icon_close").click()
                        time.sleep(2)
                    except:
                        pass

                except Exception as e:
                    print(f"Error accessing details for {name}: {e}")

            except Exception as e:
                print(f"Error processing company: {e}")

        # Scroll slightly to load more companies
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)

print(f"Data successfully saved to {csv_file}")

# Close the browser
driver.quit()
