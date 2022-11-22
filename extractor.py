from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

TARGET_URL = "https://www.sloganlist.com/fortune500-slogans-list/"
PATH = r"C:\geckodriver\geckodriver.exe"
BIN_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"


def slogan_extractor(bin_path, path, url):

    driver = webdriver.Firefox(firefox_binary=bin_path, executable_path=path)
    driver.get(url)

    tbody = driver.find_elements(By.TAG_NAME, "t")

    # [start:stops:steps]
    company = [e.text for e in tbody[::2]]
    slogan = [e.text for e in tbody[1::2]]

    if tbody:
        slogan_dict = {"company": company, "slogan": slogan}
        df = pd.DataFrame(slogan_dict)
        df.to_csv("fortune500.csv", index=False)
        driver.quit()
    else:
        print("Keine Tags gefunden!")
        driver.quit()


if __name__ == "__main__":
    slogan_extractor(BIN_PATH, PATH, TARGET_URL)
