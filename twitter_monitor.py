import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Set up Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Start ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the Twitter login page
url = 'https://x.com/i/flow/login'
driver.get(url)

# Your Twitter credentials
username_value = 'your_username'
password_value = 'your_password.'

# Locate and fill the username input field
username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username.send_keys(username_value)
username.send_keys(Keys.ENTER)

# Handle potential additional login steps (e.g., captcha, phone number, etc.)
#time.sleep(3)  # Adjust the sleep time as needed for additional steps

# Locate and fill the password input field
password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password.send_keys(password_value)
password.send_keys(Keys.ENTER)

# Wait for the profile icon to be visible as an indication of a successful login
print("Logged in successfully.")

# Navigate to Elon Musk's page
twitter_url = 'https://x.com/elonmusk'
time.sleep(2)

# Store the latest tweet ID
last_tweet_id = None

driver.get(twitter_url)
time.sleep(5)  # Wait for the page to load
print("Navigate to page successfully.")

tweets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article')))
if not tweets:
    print("No tweets found on the page.")

latest_tweet = tweets[1]

if not latest_tweet:
    print("No latest tweet found.")

tweet_link_elements = latest_tweet.find_elements(By.CSS_SELECTOR, 'a')

tweet_url = None
for link in tweet_link_elements:
    href = link.get_attribute('href')
    if 'status' in href:
        tweet_url = href
        break

tweet_content = latest_tweet.find_element(By.CSS_SELECTOR, 'div[lang]').text

if tweet_url:
    tweet_id = tweet_url.split('/')[-1]
    if tweet_id != last_tweet_id:
        last_tweet_id = tweet_id

# Get the latest tweet URL and content
latest_tweet_url, latest_tweet_content = tweet_content, tweet_url
if latest_tweet_url:
    print(f"Tweet_id: {last_tweet_id}")
    print(f"New Tweet URL: {latest_tweet_url}")
    print(f"New Tweet Content: {latest_tweet_content}")
else:
    print("No new tweet found.")
#driver.quit()
