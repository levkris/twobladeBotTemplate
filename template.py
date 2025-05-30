# Basic chatbot template
# This is a template for a twoblade chatbot.
# You can build your own chatbot using this template.
# Made by: wokki20
# https://github.com/levkris

# Messages should not contain emojis, since these are not supported by the chatbot.
# You can use the remove_non_bmp_chars function to remove non-BMP characters such as emojis.

# To import necessary libraries run:
# python3 -m pip install -r requirements.txt
# Or:
# pip3 install -r requirements.txt
# Or:
# pip install -r requirements.txt

# To run the template run:
# python3 template.py

import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

REPLIED_FILE = "yourFile.json"  # Replace with your actual file name

botName = "Your Bot Name"  # Replace with your actual bot name
botUsername = "YourBotUsername"  # Replace with your actual bot username
botPassword = "YourBotPassword"  # Replace with your actual bot password

maxMessages = 10  # Maximum number of messages to process

# Function to save full data with user included for each replied message to ensure it doesn't get replied to again
def save_replied_users_full(data_list):
    with open(REPLIED_FILE, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

# Function to check if the bot is logged in
def is_logged_in():
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "border-input")), timeout=5)
        return True
    except:
        return False
    
# Function to remove non-BMP characters such as emojis
def remove_non_bmp_chars(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)


try:
    if os.path.exists(REPLIED_FILE):
        with open(REPLIED_FILE, "r", encoding="utf-8") as f:
            replied_data = json.load(f)
    else:
        replied_data = []
        

    replied_set = set((item["text"], item["date"]) for item in replied_data)
    print(f"Loaded {len(replied_set)} replied messages from file.")

    driver.get("https://twoblade.com/chat")

    if not is_logged_in():
        driver.get("https://twoblade.com/login")

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys(botUsername)
        password_input.send_keys(botPassword)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        time.sleep(5)

        driver.get("https://twoblade.com/chat")

    textbox = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "border-input")))

    startup_message = remove_non_bmp_chars("Hello! " + botName + " is online now") # Startup message, do not include emojis
    textbox.send_keys(startup_message)
    textbox.send_keys(Keys.ENTER)

    while True:
        message_elements = driver.find_elements(By.CSS_SELECTOR, "p.overflow-wrap-anywhere.overflow-hidden.break-words.break-all.text-sm.svelte-td0eow")
        
        recent_messages = message_elements[-maxMessages:]
        
        for msg in recent_messages:
            try:
                text = remove_non_bmp_chars(msg.text.strip())

                parent = msg.find_element(By.XPATH, "..")

                try:
                    date_span = parent.find_element(By.CSS_SELECTOR, "span.text-muted-foreground.whitespace-nowrap.text-xs.svelte-td0eow")
                    date = date_span.text.strip()
                except:
                    date = "unknown"

                try:
                    user_span = parent.find_element(By.CSS_SELECTOR, "span.break-all.text-sm.font-medium.svelte-td0eow")
                    user = user_span.text.strip()
                    if user.endswith("#twoblade.com"):
                        user = user[:-len("#twoblade.com")]
                except:
                    user = "unknown_user"

                key = (text, date)
                
                if key not in replied_set:
                    print("New message from", user, "at", date, ":", text)
                    
                    replied_set.add(key)
                    replied_data.append({"text": text, "date": date, "user": user})
                    save_replied_users_full(replied_data)
                

            except Exception as e:
                import traceback
                print("Error processing message:", e)
                traceback.print_exc()


except KeyboardInterrupt:
    print(f"Shutting down {botName}...")

    driver.quit()
    print("Bye!")

except Exception as e:
    print("Error:", e)

    try:
        shutdown_msg = remove_non_bmp_chars(f"{botName} crashed! Shutting down...")
        textbox = driver.find_element(By.CLASS_NAME, "border-input")
        textbox.click()
        textbox.send_keys(shutdown_msg)
        textbox.send_keys(Keys.ENTER)
        time.sleep(2)
    except Exception as e2:
        print("Error sending crash shutdown message:", e2)

    driver.quit()
