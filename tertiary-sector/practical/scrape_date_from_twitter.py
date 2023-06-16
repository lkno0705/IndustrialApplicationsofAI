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

from nordvpn_switcher import initialize_VPN, rotate_VPN


def scrape_tweet(url: str) -> str:

    _xhr_calls = []

    def intercept_response(response):
        """capture all background requests and save them"""
        # we can extract details from background requests
        if response.request.resource_type == "xhr":
            _xhr_calls.append(response)
        return response

    with sync_playwright() as pw:
        browser: playwright.sync_api._generated.Browser = pw.chromium.launch(headless=False)
        context: playwright.sync_api._generated.BrowserContext = browser.new_context(
            viewport={"width": 1920, "height": 1080})
        page: playwright.sync_api._generated.Page = context.new_page()

        # enable background request intercepting:
        page.on("response", intercept_response)
        # go to url and wait for the page to load
        page.goto(url)
        page.wait_for_selector("[data-testid='tweet']")

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetDetail" in f.url]
        tweets = []
        for xhr in tweet_calls:
            data = xhr.json()
            xhr_tweets = nested_lookup("tweet_results", data)
            tweets.extend([tweet["result"] for tweet in xhr_tweets])

        # Now that we have all tweets, we can parse them into a thread
        # The first tweet is the parent, the rest are replies or suggested tweets
        parent = tweets.pop(0)
        # sleep to emulate reading the tweet
        slt: int = randint(10, 40)
        logging.info(f"sleeping for {slt}s")
        sleep(slt)  # sleep to emulate reading the tweet
        page.close()
        return jmespath.search("legacy.created_at", parent)


if __name__ == "__main__":

    initialize_VPN(area_input=['complete rotation'])
    # logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if len(sys.argv) > 1:

        # use random sampling of numbers and sleep times to obfuscate scraping activity
        # number_of_tweets_before_sleep: int = randint(5, 20)
        # logging.info(f"{number_of_tweets_before_sleep} before sleeping")

        result: List[Tuple[str, datetime]] = []

        for cnt, url in tqdm(enumerate(sys.argv[1:], start=1)):
            result.append((url, datetime.strptime(scrape_tweet(str(url)),
                                                  "%a %b %d %H:%M:%S %z %Y")))  # scrape current url

            if cnt % 5 == 0:
                rotate_VPN()
            # sleep after sampled number of tweets to obfuscate scraping
            # if cnt % number_of_tweets_before_sleep == 0:
            #
            #     number_of_tweets_before_sleep = randint(5, 20)
            #     slt = randint(30, 60)
            #     logging.info(f"sleeping for {slt}s")
            #     sleep(slt)
            #     logging.info(f"{number_of_tweets_before_sleep} before sleeping")
        pd.DataFrame(result, columns=["url", "datetime"]).to_csv("./datasets/scraped_twitter_dates.csv", index=False)
