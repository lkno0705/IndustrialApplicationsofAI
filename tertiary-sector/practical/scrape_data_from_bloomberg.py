import os
import sys

import logging
from typing import Dict, List, Tuple

import jmespath
import pandas as pd
import playwright.sync_api._generated
from playwright.sync_api import sync_playwright
from nested_lookup import nested_lookup
from tqdm import tqdm

from datetime import datetime

from time import sleep
from random import randint
import regex as re

from nordvpn_switcher import initialize_VPN, rotate_VPN

def scrape_bloomberg(url: str) -> str:
    with sync_playwright() as pw:
        browser: playwright.sync_api._generated.Browser = pw.chromium.launch(headless=False)
        context: playwright.sync_api._generated.BrowserContext = browser.new_context(
            viewport={"width": 1920, "height": 1080})

        page: playwright.sync_api._generated.Page = context.new_page()

        # go to url and wait for the page to load
        page.goto(url, timeout=60000)
        page.wait_for_load_state()
        match = re.search(r'(?:<time itemprop="datePublished" datetime=")(\d{4}-\d{2}-\d{2})', page.content()).groups()[
            0]
        slt: int = randint(10, 40)
        logging.info(f"sleeping for {slt}s")
        sleep(slt)  # sleep to emulate reading the tweet
        browser.close()
        return match


if __name__ == "__main__":

    initialize_VPN(save=1, area_input=['complete rotation'])

    # logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if len(sys.argv) > 1:

        # use random sampling of numbers and sleep times to obfuscate scraping activity
        number_of_requests_before_sleep: int = randint(5, 20)
        logging.info(f"{number_of_requests_before_sleep} before sleeping")

        result: List[Tuple[str, datetime]] = []

        for cnt, url in tqdm(enumerate(sys.argv[1:], start=1)):
            try:
                date = datetime.strptime(scrape_bloomberg(str(url)), "%Y-%m-%d")
            except:
                logging.warning(f"Could not extract date for URL: {url}")
                date = None

            result.append((url, date))  # scrape current url

            if cnt % 5 == 0:
                rotate_VPN()
            # sleep after sampled number of requests to obfuscate scraping
            # if cnt % number_of_requests_before_sleep == 0:
            #     number_of_requests_before_sleep = randint(5, 20)
            #     slt = randint(30, 60)
            #     logging.info(f"sleeping for {slt}s")
            #     sleep(slt)
            #     logging.info(f"{number_of_requests_before_sleep} before sleeping")
        pd.DataFrame(result, columns=["url", "datetime"]).to_csv("datasets/scraped_bloomberg_dates.csv", index=False)
