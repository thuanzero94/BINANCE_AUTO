from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import utils
from subprocess import Popen, PIPE
import re, os, time, sys
import shutil
from selenium.webdriver.chrome.options import Options

FAIL = 0
SUCCESS = 1


if __name__ == '__main__':
    chrome_port = 9022  # Default chrome_port
    chrome_driver = "C:\selenium\chromedriver.exe"
    if len(sys.argv) < 2:
        print("Usage: python auto_binance.py [key_code] [chrome_port] [chrome_driver_path]")
        exit(-1)
    if len(sys.argv) > 3:
        chrome_port = sys.argv[2]
        chrome_driver = sys.argv[3]

    key_code = sys.argv[1]

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:" + chrome_port)

    browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    print(browser.title)

    search = browser.find_element_by_id("SearchInput-input-search")
    search.clear()
    search.send_keys(key_code)
    time.sleep(0.2)

    target = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div/a/div[2]')
    target.click()
    buy_75 = browser.find_element(By.XPATH, '//*[@id="OrderForm-input-Buy-75"]')
    buy_75.click()
