from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
import yaml


def credentials():      # Load Credentials of Facebook
    with open('credentials.yml', 'r') as dataFlow:  # Opening the File
        try:
            data = str(yaml.safe_load(dataFlow)).split("'")     # Loading Data
            URL = data[5]
            username = data[9]
            password = data[13]
            # for i in range(len(data)):
            #     print(f"data{[i]}: {data[i]}")

        except yaml.YAMLError as exc:
            print(exc)
    return URL, username, password



def main():
    URL, username, password = credentials()
    print(f"Website URL: {URL}")
    print(f"UserName: {username}")
    print(f"Password: {password}")

    driver = webdriver.Chrome()     # Load Chrome Drivers
    driver.get(URL)                 # Go to the Facebook Website

    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.XPATH, "//div[@class = '_6ltg']//button").click()    # Logging In

    x = 10
    time.sleep(x)     # Wait for x seconds and then close the program

if __name__=="__main__":
    main()