# Twitter/X Influencer Post Monitor

## Overview

This project is a web crawler designed to monitor tweets/replies from a specific Twitter/X influencer, such as Elon Musk. The crawler logs into Twitter, navigates to the influencer's page, and retrieves the latest tweet's URL and content. The project uses Selenium WebDriver for automation and interaction with the web page.

## Features

- Uses ChromeDriver to open a headless window
- Automated login to Twitter
- Navigation to a specified Twitter influencer's page
- Retrieval of the latest tweet's URL and content
- Detection of changes in tweets to identify new posts
- Extracts the information of new post/reply and pushes it to WeChat bot via API

## Prerequisites

- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Setup

1. **Install Selenium:**
   ```sh
   pip install selenium
   
2. **Download ChromeDriver:**
   
   Download the version of [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) that matches your Chrome browser version from here.
   Add the ChromeDriver executable to your system PATH or specify its location in your script.

3. **Clone the Repository:**
   ```
   https://github.com/jesse980107/X.git
## Usage
1. **Update Credentials:**
   
   Replace username_value and password_value with your Twitter credentials in the script.

2. **Run the Script:**
   ```
   python twitter_monitor.py
    
