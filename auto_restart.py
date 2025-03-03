import time as t
import traceback
from bs4 import BeautifulSoup
from selenium import webdriver
import edgedriver_autoinstaller
import json
import pandas as pd
import os


def setup_driver():
    """Sets up the Edge WebDriver with necessary options."""
    edgedriver_autoinstaller.install()
    options = webdriver.EdgeOptions()
    options.add_argument('--inprivate')
    return webdriver.Edge(options=options)


def solve_captcha(driver):
    timeout = 180
    start_time = t.time()

    while True:
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        captcha_detected = soup.find('div', id='captcha-container')

        if captcha_detected:
            print(f"CAPTCHA detected. Elapsed time: {t.time() - start_time:.2f} sec")
            if t.time() - start_time > timeout:
                print("CAPTCHA timeout reached. Refreshing page...")
                driver.refresh()
                t.sleep(10)
                start_time = t.time()
            else:
                print("Please solve the CAPTCHA manually (press Enter when done)...")
                input()
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                captcha_detected = soup.find('div', id='captcha-container')
                if not captcha_detected:
                    print("CAPTCHA solved. Continuing...")
                    return soup
        else:
            return soup


def run_scraper():
    """Runs the parkrun scraper."""
    driver = setup_driver()
    events = pd.read_csv('Main Scraper/eventnames_full.csv')

    try:
        for event in events['eventname']:
            url = f'https://www.parkrun.ie/{event}/results/latestresults/'
            print(f'Scraping Parkrun event: {event}')
            driver.get(url)

            soup = solve_captcha(driver)

            number_element = int(soup.find('div', class_='aStat').find(
                'span', class_='num').text.strip())

            file_path = rf'C:\Users\odonnellpaddy\OneDrive - Meta\Parkrun 2\scraped_files\{event}.json'
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                last_scraped_number = existing_data[1]['Event Number'] if existing_data else 0
            else:
                existing_data = []
                last_scraped_number = 0

            # Only scrape new events
            numbers = range(number_element, last_scraped_number, -1)
            all_runners = []

            for number in numbers:
                url = f'https://www.parkrun.ie/{event}/results/{number}/'
                print(f'Scraping {event} number: {number}')
                driver.get(url)

                soup = solve_captcha(driver)

                date_element = soup.find('span', class_='format-date')
                date = date_element.text.strip() if date_element else 'unknown date'

                location_element = soup.find('h1')
                location = location_element.text.strip(
                )[:-8] if location_element else 'unknown location'

                timeout = 30
                start_time = t.time()

                while True:
                    soup = solve_captcha(driver)
                    table = soup.find('table')
                    if table:
                        break
                    if t.time() - start_time > timeout:
                        print(
                            f'Timeout: No table found for event number: {number}')
                        break

                    print(f'Retrying event number: {number}...')
                    t.sleep(2)
                    driver.get(url)

                if not table:
                    continue

                rows = table.find_all('tr', class_='Results-table-row')

                # Extract event number from the page
                event_number_element = soup.find(
                    'span', text=lambda x: x and x.startswith('#'))
                if event_number_element:
                    number_element_b = int(event_number_element.text.strip('#'))
                else:
                    print(f"Could not extract event number for event: {number}")
                    continue

                for row in rows:
                    name = row.get('data-name', 'Unknown')
                    age_group = row.get('data-agegroup', 'Unknown')
                    club = row.get('data-club', 'N/A')
                    gender = row.get('data-gender', 'Unknown')
                    position = row.get('data-position', 'N/A')
                    runs = row.get('data-runs')
                    vols = row.get('data-vols', '0')
                    age_grade = row.get('data-agegrade', '0.00')

                    time_cell = row.find('td', class_='Results-table-td--time')
                    time = time_cell.find('div', class_='compact').text.strip(
                    ) if time_cell and time_cell.find('div') else 'N/A'

                    club_cell = row.find('td', class_='Results-table-td--club')
                    club_link = club_cell.find('div', class_='compact').text.strip(
                    ) if club_cell and club_cell.find('div') else 'N/A'

                    # Extract parkrunner ID
                    a_tag = row.find('a', href=True)
                    parkrunner_id = None
                    if a_tag:
                        href = a_tag['href']
                        parkrunner_id = href.split('/parkrunner/')[1]

                    all_runners.append({
                        'Name': name,
                        'Parkrunner ID': parkrunner_id,
                        'Age Group': age_group,
                        'club': club,
                        'Gender': gender,
                        'Position': position,
                        'Runs': runs,
                        'Volunteers': vols,
                        'Age Grade': age_grade,
                        'Time': time,
                        'Club Link': club_link,
                        'Location': location,
                        'Date': date,
                        'Event Number': number_element_b
                    })

            # Append new runners to existing data
            existing_data = all_runners + existing_data
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=4, ensure_ascii=False)
            print(f'Saved data for event: {event} to {event}.json')

    except Exception as e:
        print(f"Scraper crashed with error: {e}")
        print(traceback.format_exc())

    finally:
        driver.quit()


if __name__ == "__main__":
    max_retries = 50
    retry_count = 0

    while retry_count < max_retries:
        try:
            run_scraper()
            break  # Exit loop if successful
        except Exception as e:
            print(f"Scraper crashed. Restarting in 60 seconds... (Attempt {retry_count + 1}/{max_retries})")
            print(f"Error: {e}")
            print(traceback.format_exc())
            retry_count += 1
            t.sleep(60)  # Wait before retrying

    if retry_count == max_retries:
        print("Max retries reached. Scraper failed.")
