import threading
import csv
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Global flag to stop the program
stop_scraping = False

def monitor_for_exit():
    """Waits for user input to stop the program."""
    global stop_scraping
    input("Press ENTER at any time to stop the program.\n")
    stop_scraping = True

# Start the thread to listen for the stop command
exit_thread = threading.Thread(target=monitor_for_exit)
exit_thread.daemon = True  # This allows the thread to exit when the main program exits
exit_thread.start()

# Set up browser options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver_path = "/Users/monika/Desktop/git/PythonProjects/PythonsOfWonder/TubeTalks/chromedriver-mac-arm64/chromedriver"  # Update path to your chromedriver

# Initialize the WebDriver using Service
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://www.youtube.com/watch?v=iFPMz36std4')
    
    # Initial scroll to load comments section
    driver.execute_script('window.scrollTo(0, 500);')
    time.sleep(2)  # Wait for comments to load

    # Prepare list to store comments
    items = []
    
    # Initialize timeout variables
    max_wait_time = timedelta(hours=1)  # Set to 1 hour
    start_time = datetime.now()
    last_comment_count = 0  # Track the count of comments in the previous loop

    # Scroll to load more comments dynamically
    scroll_count = 0
    while not stop_scraping:
        driver.execute_script('window.scrollBy(0, 3000);')
        time.sleep(2)
        scroll_count += 1
        print(f"Scroll #{scroll_count} completed.")

        # Extract current comments
        username_elems = driver.find_elements(By.XPATH, '//*[@id="author-text"]')
        comment_elems = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        
        # If new comments are added, reset the timer
        if len(comment_elems) > last_comment_count:
            start_time = datetime.now()  # Reset the timeout
            last_comment_count = len(comment_elems)  # Update the last comment count
            print(f"New comments found. Total comments: {last_comment_count}")

        # Check if 1 hour has passed without new comments
        elif datetime.now() - start_time > max_wait_time:
            print("No new comments for 1 hour. Stopping the program.")
            break

    # Collect data
    for username, comment in zip(username_elems, comment_elems):
        item = {
            'Author': username.text.strip(),
            'Comment': comment.text.strip()
        }
        items.append(item)

    # Export to CSV
    filename = './commentlist.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Author', 'Comment'])
        writer.writeheader()
        writer.writerows(items)

    print(f"Successfully saved {len(items)} comments to {filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed. Program terminated.")
